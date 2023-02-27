class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.item_count = len(data)

    @property
    def page_count(self):
        return (self.item_count + self.items_on_page - 1) // self.items_on_page

    def count_items_on_page(self, page_number):
        if page_number >= self.items_on_page:
            raise Exception ("Wrong number. Page is missing!")
        first_index = page_number * self.items_on_page
        last_index = first_index + self.items_on_page
        return len(self.data[first_index:last_index])

    def find_page(self, data):
        if data not in self.data:
            raise Exception(f"'Error. {data}' is missing pages")
        results = []
        start_index = 0
        while True:
            index = self.data.find(data, start_index)
            if index == -1:
                break
            page_number = index // self.items_on_page
            results.append(page_number)
            start_index = index + 1
        return results
    
    def display_page(self, page_number):
        if page_number >= self.page_count:
            raise Exception("Error: Invalid index. Page is missing")
        start_index = page_number * self.items_on_page
        end_index = start_index + self.items_on_page
        return self.data[start_index:end_index]


