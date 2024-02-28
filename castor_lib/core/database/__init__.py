"""Base class for database operations."""

from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.results import InsertOneResult, UpdateResult, DeleteResult
from castor_lib.core.logging import get_logger
from castor_lib.core.models import ActivityLog, \
        Agent, Attachment, Check, Client, Command, \
        Comment, Expense, Job, Notification, Permission, \
        Preference, Project, Role, Screenshot, Secret, \
        Tag, Task, User

# Create a map of model classes to collection names
COLLECTION_MAP = {
    ActivityLog: 'activity_logs',
    Agent: 'agents',
    Attachment: 'attachments',
    Check: 'checks',
    Client: 'clients',
    Command: 'commands',
    Comment: 'comments',
    Expense: 'expenses',
    Job: 'jobs',
    Notification: 'notifications',
    Permission: 'permissions',
    Preference: 'preferences',
    Project: 'projects',
    Role: 'roles',
    Screenshot: 'screenshots',
    Secret: 'secrets',
    Tag: 'tags',
    Task: 'tasks',
    User: 'users'
}

class DatabaseConfig(BaseModel):
    """Database configuration."""
    host: str = 'localhost'
    port: int = 27017
    username: str | None = None
    password: str | None = None
    auth_database: str = 'admin'
    database: str = 'castor'


class CastorDatabase():
    """Base class for database operations.

    This class should abstract MongoDB operations and provide a consistent
    interface for interacting with the database. It should also provide
    logging and error handling for database operations.
    """

    def __init__(self, config: DatabaseConfig) -> None:
        self.config = config
        self.logger = get_logger(__name__)
        self.client = MongoClient(config.host,
                                    username=config.username,
                                    password=config.password,
                                    authSource=config.auth_database,
                                    authMechanism='SCRAM-SHA-256')
        self.db = self.client[config.database]
        self.logger.info('Database client initialized')

    def connect(self) -> None:
        """Connect to the database."""
        self.logger.debug('Connecting to the database')
        self.client.server_info()  # Test connection
        self.logger.debug('Connected to the database')

    def disconnect(self) -> None:
        """Disconnect from the database."""
        self.logger.debug('Disconnecting from the database')
        self.client.close()
        self.logger.debug('Disconnected from the database')

    def _insert(self, collection: str, document: dict) -> InsertOneResult:
        """Insert a document into a collection."""
        self.logger.debug(f'Inserting document into {collection}')
        result = self.db[collection].insert_one(document)
        self.logger.debug(f'Document inserted into {collection}')
        return result

    def _find(self, collection: str, query: dict) -> list[dict]:
        """Find documents in a collection."""
        self.logger.debug(f'Finding documents in {collection}')
        documents = list(self.db[collection].find(query))
        self.logger.debug(f'Found {len(documents)} documents in {collection}')
        return documents

    def _update(self, collection: str, query: dict, update: dict) -> UpdateResult:
        """Update documents in a collection."""
        self.logger.debug(f'Updating documents in {collection}')
        # Received query is just the key and value that need to update
        # So, we need to convert it to the full query with $set
        update = {'$set': update}
        result = self.db[collection].update_one(query, update)
        self.logger.debug(f'Updated documents in {collection}')
        return result

    def _delete(self, collection: str, query: dict) -> DeleteResult:
        """Delete documents from a collection."""
        self.logger.debug(f'Deleting documents from {collection}')
        result = self.db[collection].delete_many(query)
        self.logger.debug(f'Deleted documents from {collection}')
        return result

    def _get_collection(self, collection: str) -> list[dict]:
        """Get all documents from a collection."""
        return self._find(collection, {})

    # Use the COLLECTION_MAP to access the correct collection for each model
    # class and do type casting to the model class when returning the results
    def get_collection(self, model: BaseModel) -> list[dict]:
        """Get all documents from a collection."""
        collection = COLLECTION_MAP[model]
        return [model(**doc) for doc in self._get_collection(collection)]

    def insert(self, model: BaseModel, data: BaseModel) -> InsertOneResult:
        """Insert a document into the database."""
        collection = COLLECTION_MAP[model]
        result = self._insert(collection, dict(data))
        return result

    def delete(self, model: BaseModel, data: BaseModel) -> DeleteResult:
        """Delete a document from the database."""
        collection = COLLECTION_MAP[model]
        self._delete(collection, dict(data))

    def find(self, model: BaseModel, query: dict) -> list[BaseModel]:
        """Find documents in the database."""
        collection = COLLECTION_MAP[model]
        return [model(**doc) for doc in self._find(collection, query)]

    def update(self, model: BaseModel, query: dict, update: dict) -> UpdateResult:
        """Update documents in the database."""
        collection = COLLECTION_MAP[model]
        result = self._update(collection, query, update)
        return result

    def get(self, model: BaseModel, query: dict) -> BaseModel:
        """Get a document from the database."""
        collection = COLLECTION_MAP[model]
        return model(**self._find(collection, query)[0])

    def get_by_id(self, model: BaseModel, _id: str) -> BaseModel:
        """Get a document from the database by its ID."""
        query = {'_id': _id}
        return self.get(model, query)

    def get_by_name(self, model: BaseModel, name: str) -> BaseModel:
        """Get a document from the database by its name."""
        query = {'name': name}
        return self.get(model, query)
