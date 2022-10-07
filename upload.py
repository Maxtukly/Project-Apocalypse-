
class Upload:
    def __init__(self, p, os):
        self.p = p
        self.os = os
        print('started: upload')

    def upload_textures(self, filepath):
        print('uploading...')
        ret_list = []
        count = 0
        # for path in self.os.listdir(filepath):
        #     if self.os.path.isfile(self.os.path.join(filepath, path)):
        #         count += 1
        files_list = self.os.listdir(filepath)
        for i in files_list:
            ret_list += self.p.image.load(filepath + str(i)).convert()
        print('uploaded')
        return ret_list



