from office365.entity import Entity
from office365.runtime.client_result import ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery


class GroupLifecyclePolicy(Entity):
    """
    Represents a lifecycle policy for a Microsoft 365 group. A group lifecycle policy allows administrators
    to set an expiration period for groups. For example, after 180 days, a group expires.
    When a group reaches its expiration, owners of the group are required to renew their group within a time interval
    defined by the administrator. Once renewed, the group expiration is extended by the number of days defined
    in the policy. For example, the group's new expiration is 180 days after renewal.
    If the group is not renewed, it expires and is deleted.
    The group can be restored within a period of 30 days from deletion.
    """

    def add_group(self, group_id):
        """
        Adds specific groups to a lifecycle policy. This action limits the group lifecycle policy to a set of groups
        only if the managedGroupTypes property of groupLifecyclePolicy is set to Selected.

        :param str group_id: The identifier of the group to remove from the policy.
        """
        return_type = ClientResult(self.context, bool())
        payload = {"groupId": group_id}
        qry = ServiceOperationQuery(self, "addGroup", None, payload, None, return_type)
        self.context.add_query(qry)
        return return_type

    def remove_group(self, group_id):
        """
        Removes a group from a lifecycle policy.

        :param str group_id: The identifier of the group to add to the policy.
        """
        return_type = ClientResult(self.context, bool())
        payload = {"groupId": group_id}
        qry = ServiceOperationQuery(self, "removeGroup", None, payload, None, return_type)
        self.context.add_query(qry)
        return return_type

    @property
    def managed_group_types(self):
        """The group type for which the expiration policy applies. Possible values are All, Selected or None."""
        return self.properties.get("managedGroupTypes", None)
