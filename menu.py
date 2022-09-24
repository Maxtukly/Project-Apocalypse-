class Menu:
    def __init__(self, p, screen, msg='no massage'):
        self.p = p
        self.screen = screen
        print(msg) 
        pixelfont = p.font.Font('./font/Grand9K Pixel.ttf', 62)
        self.max = 'Hello, The Vest DM, Max'
        self.printed = ''
        self.times = 0
        
    #def start_menu_loading(self, time):
        
        