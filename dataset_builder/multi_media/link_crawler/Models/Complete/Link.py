from link_crawler.Models.Model import Model


class Link(Model):
     

    def __init__(self,run_dir):
        Model.__init__(self)
        self.file_path=run_dir+"/complete_link.txt"
        self.fetch()

