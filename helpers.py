titles = dict()
titles['IronMan1'] = 'Iron Man'
titles['IronMan2'] = 'Iron Man 2'
titles['IronMan3'] = 'Iron Man 3'
titles['CaptainAmerica1'] = 'Captain America: The First Avenger'
titles['CaptainAmerica2'] = 'Captain America: The Winter Soldier'
titles['CaptainAmerica3'] = 'Captain America: Civil War'
titles['Thor1'] = 'Thor'
titles['Thor2'] = 'Thor: The Dark World'
titles['Thor3'] = 'Thor: Ragnarok'
titles['Hulk'] = 'The Incredible Hulk'
titles['AntMan1'] = 'Ant-Man'
titles['AntMan2'] = 'Ant-Man and the Wasp'
titles['GOTG1'] = 'Guardians of the Galaxy'
titles['GOTG2'] = 'Guardians of the Galaxy Vol. 2'
titles['SpiderMan1'] = 'Spider-Man: Homecoming'
titles['SpiderMan2'] = 'Spider-Man: Far From Home'
titles['DrStrange'] = 'Doctor Strange'
titles['CaptainMarvel'] = 'Captain Marvel'
titles['BlackPanther'] = 'Black Panther'
titles['Avengers1'] = 'The Avengers'
titles['Avengers2'] = 'Avengers: Age of Ultron'
titles['Avengers3'] = 'Avengers: Infinity War'
titles['Avengers4'] = 'Avengers: Endgame'
titles['JurassicPark'] = 'Jurrasic Park'
titles['WizardOfOz'] = 'The Wizard of Oz'
titles['FindingNemo'] = 'Finding Nemo'
titles['Pyscho'] = 'Pyscho'

def getTitles():
    titleArr = ['Avengers1', 'Avengers2', 'Avengers3', 'Avengers4',
                'IronMan1', 'IronMan2', 'IronMan3',
                'CaptainAmerica1', 'CaptainAmerica2', 'CaptainAmerica3',
                'Thor1', 'Thor2', 'Thor3',
                'AntMan1', 'AntMan2',
                'GOTG1', 'GOTG2',
                'SpiderMan1', 'SpiderMan2',
                'Hulk',
                'DrStrange',
                'CaptainMarvel',
                'BlackPanther',
                'JurassicPark',
                'WizardOfOz',
                'FindingNemo',
                'Pyscho']
    return titleArr


def getCorrectTitle(movie):
    return titles[movie]

def getPossInputs():
    output = ''
    output += 'Avengers1 Avengers2 Avengers3 Avengers4\n'
    output += 'IronMan1 IronMan2 IronMan3\n'
    output += 'CaptainAmerica1 CaptainAmerica2 CaptainAmerica3\n'
    output += 'Thor1 Thor2 Thor3\n'
    output += 'AntMan1 AntMan2\n'
    output += 'GOTG1 GOTG2\n'
    output += 'SpiderMan1 SpiderMan2\n'
    output += 'Hulk\n'
    output += 'DrStrange\n'
    output += 'CaptainMarvel\n'
    output += 'BlackPanther\n'
    output += 'Jurassicpark\n'
    output += 'WizardOfOz\n'
    output += 'FindingNemo\n'
    output += 'Pyscho\n'

    return output
    
    
