import os

class file_writer:
    Attribute_file = "attributes.json"

    def write(self, cis):
        self.__create_toplevel_dir(cis)
        self.__write_class_metadata(cis)

        path = self.__create_toplevel_image_dir(cis)
        for i in cis.get_images():
            self.__write_image(path, cis.get_image(i))
            
    def __create_toplevel_channel_dir(self, path):
        path = os.path.join( path, "channel" )
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of {} failed".format(path))

        return path 

    def __create_channel_dir(self, path, channel):
        path = os.path.join( path, channel.name )
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of {} failed".format(path))

        return path 

    def __create_toplevel_layer_dir(self, path, image):
        path = os.path.join( path, image.name, "layer" )
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of {} failed".format(path))

        return path 

    def __create_layer_dir(self, path, layer):
        path = os.path.join( path, layer.name )
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of {} failed".format(path))

        return path 


    def __create_image_dir(self, path, image):
        path = os.path.join( path, image.name )
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of {} failed".format(path))

        return path

    def __create_toplevel_image_dir(self, cis):
        path = os.path.join( cis.fname, "image" )
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of {} failed".format(path))

        return path

    def __create_toplevel_dir(self, cis):
        path = cis.fname
        try:
            os.makedirs(cis.fname)
        except OSError:
            print("Creation of {} failed".format(cis.fname))

        return path

    def __write_class_metadata(self, cis):
        with open(os.path.join( cis.fname, self.Attribute_file), "w") as f:
            f.write("{\n")
            f.write("  classname : \"{}\",\n".format(cis.classname))
            f.write("  dims      : [{}, {}],\n".format(cis.dims[0], cis.dims[1]))
            f.write("  version   : \"{}\",\n".format(cis.version))
            f.write("  flags     : \"{}\",\n".format(cis.flags))
            f.write("  origin    : \"{}\"\n".format(cis.origin))
            f.write("}\n")

    def __write_layer_metadata(self, path, layer):
        with open(os.path.join( path, self.Attribute_file), "w") as f:
            f.write("{\n")
            f.write("  offset : [{}, {}],\n".format(layer.offset[0], layer.offset[1]))
            f.write("  dims   : [{}, {}],\n".format(layer.dims[0], layer.dims[1]))
            f.write("}\n")

    def __write_image(self, path, image):
        self.__create_image_dir(path, image)
        path = self.__create_toplevel_layer_dir(path, image)

        for l in image.get_layers():
            self.__write_layer(path, image.get_layer(l))

        
    def __write_layer(self, path, layer):
        path = self.__create_layer_dir(path, layer)
        self.__write_layer_metadata(path, layer) 
        path = self.__create_toplevel_channel_dir(path)

        for c in layer.get_channels():
            self.__create_channel_dir(path, layer.get_channel(c))
