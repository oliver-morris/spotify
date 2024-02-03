
class ItemList:
    def __init__(self, items):
        self.items = items

    def add(self, item):
        self.items.append(item)

    def names(self):
        names_list = []
        for item in self.items:
            names_list.append(item.name)
        return names_list

    def ids(self):
        ids_list = []
        for item in self.items:
            ids_list.append(item.id)
        return ids_list

    def urls(self):
        urls_list = []
        for item in self.items:
            urls_list.append(item.url)
        return urls_list

    def length(self):
        return len(self.items)