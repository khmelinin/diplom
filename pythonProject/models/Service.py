class Service:

    def __int__(self):
        self.service_directory_id = -1
        self.name = ''
        self.name_gost  = ''
        self.description = ''
        self.price = -1

    def __int__(self, sd_id, n, n_g, d, p):
        self.service_directory_id = sd_id
        self.name = n
        self.name_gost  = n_g
        self.description = d
        self.price = p

