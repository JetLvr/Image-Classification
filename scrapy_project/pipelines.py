from scrapy.pipelines.images import ImagesPipeline
import os

class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):

        file_name = item['text']
        file_path = f'local_folder/full/{file_name}.jpg'

        if os.path.exists(file_path):
            i = 1
            while True:
                new_path = f'full/{file_name}({i}).jpg'
                if os.path.exists(f'local_folder/{new_path}'):
                    i += 1
                else:
                    return new_path
        else:
            return f'full/{file_name}.jpg'