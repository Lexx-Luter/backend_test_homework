def Running():
    print('Running')

def SportsWalking():
    print('SportsWalking')

def Swimming():
    print('Swimming')

workout_type = 'SWM'
    
type_tren_dic = {
    'RUN': Running,
    'WLK': SportsWalking,
    'SWM': Swimming
    }
type_tren_dic[workout_type]()
