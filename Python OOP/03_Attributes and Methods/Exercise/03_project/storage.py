from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    categories: List
    topics: List
    documents: List

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        category_names = [c.name for c in self.categories]
        if category.name not in category_names:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        topic_names = [t.topic for t in self.topics]
        if topic.topic not in topic_names:
            self.topics.append(topic)

    def add_document(self, document: Document):
        document_names = [d.file_name for d in self.documents]
        if document.file_name not in document_names:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for category in self.categories:
            if category.id == category_id:
                category.name = new_name

    def edit_topics(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category_ids = [c.id for c in self.categories]
        if category_id in category_ids:
            self.categories.pop(category_ids.index(category_id))

    def delete_topic(self, topic_id: int):
        topic_ids = [t.id for t in self.topics]
        if topic_id in topic_ids:
            self.topics.pop(topic_ids.index(topic_id))

    def delete_document(self, document_id: int):
        document_ids = [d.id for d in self.documents]
        if document_id in document_ids:
            self.documents.remove(document_ids.index(document_id))

    def get_document(self, document_id: int):
        document_ids = [d.id for d in self.documents]
        if document_id in document_ids:
            return self.documents[document_ids.index(document_id)]

    def __repr__(self) -> str:
        documents = list(map(str, self.documents))
        return "\n".join(documents)
