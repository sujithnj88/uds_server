from base_class import BaseDecoder, BaseEncoder


class SecurityAccess(BaseDecoder, BaseEncoder):
    def __init__(self):
        super(BaseDecoder, self).__init__()
        super(BaseEncoder, self).__init__()