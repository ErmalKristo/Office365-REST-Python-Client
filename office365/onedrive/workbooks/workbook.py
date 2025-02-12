from office365.entity import Entity
from office365.entity_collection import EntityCollection
from office365.onedrive.workbooks.applications.application import WorkbookApplication
from office365.onedrive.workbooks.comments.comment import WorkbookComment
from office365.onedrive.workbooks.functions.functions import WorkbookFunctions
from office365.onedrive.workbooks.names.named_item import WorkbookNamedItem
from office365.onedrive.workbooks.operations.workbook import WorkbookOperation
from office365.onedrive.workbooks.session_info import WorkbookSessionInfo
from office365.onedrive.workbooks.tables.collection import WorkbookTableCollection
from office365.onedrive.workbooks.worksheets.collection import WorkbookWorksheetCollection
from office365.runtime.client_result import ClientResult
from office365.runtime.paths.resource_path import ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery


class Workbook(Entity):
    """The top-level object that contains related workbook objects such as worksheets, tables, and ranges."""

    def session_info_resource(self):
        return_type = ClientResult(self.context, WorkbookSessionInfo())
        qry = ServiceOperationQuery(self, "sessionInfoResource", None, None, None, return_type)
        self.context.add_query(qry)
        return return_type

    def create_session(self):
        """
        Create a new workbook session.

        Excel APIs can be called in one of two modes:
            Persistent session - All changes made to the workbook are persisted (saved). This is the usual mode of
                operation.
            Non-persistent session - Changes made by the API are not saved to the source location. Instead, the Excel
                backend server keeps a temporary copy of the file that reflects the changes made during that particular
                API session. When the Excel session expires, the changes are lost. This mode is useful for apps that
                need to do analysis or obtain the results of a calculation or a chart image, but not affect the
                document state.
        """
        return_type = ClientResult(self.context, WorkbookSessionInfo())
        qry = ServiceOperationQuery(self, "createSession", None, None, None, return_type)
        self.context.add_query(qry)
        return return_type

    def refresh_session(self):
        """Use this API to refresh an existing workbook session."""
        qry = ServiceOperationQuery(self, "refreshSession")
        self.context.add_query(qry)
        return self

    def close_session(self):
        """Use this API to close an existing workbook session."""
        qry = ServiceOperationQuery(self, "closeSession")
        self.context.add_query(qry)
        return self

    @property
    def application(self):
        """"""
        return self.properties.get('application',
                                   WorkbookApplication(self.context, ResourcePath("application", self.resource_path)))

    @property
    def comments(self):
        """"""
        return self.properties.get('comments',
                                   EntityCollection(self.context,
                                                    WorkbookComment, ResourcePath("comments", self.resource_path)))

    @property
    def functions(self):
        """"""
        return self.properties.get('functions',
                                   WorkbookFunctions(self.context, ResourcePath("functions", self.resource_path)))

    @property
    def tables(self):
        """Represents a collection of tables associated with the workbook. Read-only."""
        return self.properties.get('tables',
                                   WorkbookTableCollection(self.context, ResourcePath("tables", self.resource_path)))

    @property
    def names(self):
        """Represents a collection of workbook scoped named items (named ranges and constants). Read-only."""
        return self.properties.get('names',
                                   EntityCollection(self.context, WorkbookNamedItem,
                                                    ResourcePath("names", self.resource_path)))

    @property
    def operations(self):
        """The status of workbook operations. Getting an operation collection is not supported, but you can get the
        status of a long-running operation if the Location header is returned in the response"""
        return self.properties.get('operations',
                                   EntityCollection(self.context, WorkbookOperation,
                                                    ResourcePath("operations", self.resource_path)))

    @property
    def worksheets(self):
        """Represents a collection of worksheets associated with the workbook. Read-only."""
        return self.properties.get('worksheets',
                                   WorkbookWorksheetCollection(self.context,
                                                               ResourcePath("worksheets", self.resource_path)))
