import configparser

class ReadCfg():
    def __init__(self, config_file):
        """
        :param config_file: Configuration file
        """
        self.config_file = config_file
        #self.lines = lines

    def read_section(self):
        """
        :return: Return sections from configuration file
        """
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return [section for section in config.sections()]

    def read_values(self, section):
        """
        :param section: Sections from the configuration file
        :return: Return values of sections
        """
        config = configparser.ConfigParser()
        config.read(self.config_file)
        if isinstance(section, str):
            return dict(config.items(section))
        else:
            return [[variable for variable in dict(config.items(item))] for item in section]

    def concat_values(self, *args):
        return ''.join(args)



