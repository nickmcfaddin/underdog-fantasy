import random

def Parlay(legs, percent, wager, startingBankroll, free):

    #Setup variables
    fullList = list(range(1, 101))
    hit = True
    i = 0

    while i < legs:

        #Removes leg calculation for free squares
        if (free > 0):
            i = i + free

        #Picks random number, if in your hit range proceed, else lay misses
        rand = random.choice(fullList)
        if(rand >= percent):
            hit = False
        i = i + 1
    
    #Modifies bankroll based on hit/miss
    if (hit == False):
        bankroll2 = startingBankroll - (1*wager)
    else:
        if (legs == 2):
            bankroll2 = startingBankroll + (3*wager)
        if (legs == 3):
            bankroll2 = startingBankroll + (6*wager)
        if (legs == 4):
            bankroll2 = startingBankroll + (10*wager)
        if (legs == 5):
            bankroll2 = startingBankroll + (20*wager)

    if(bankroll2 < 0):
        bankroll2 = 0

    return bankroll2

def TrialSet(legs, percent, bankroll, wager):
    #Testing variables
    trials = 1000
    counter = 0

    #If you have consistent free bets in each bet you make
    free = 0
    
    #Setup variables
    legs2 = int(legs)
    percent2 = int(percent)
    bankroll2 = int(bankroll)
    wager2 = int(wager)

    bankrupt = 0
    
    while counter < trials:
        if(bankroll2 > wager2):
            bankroll2 = Parlay(legs2, percent2, wager2, bankroll2, free)
            counter = counter + 1
        else:
            bankrupt = counter + 1
            break

    if(bankrupt == 0):
        print(f'Over the course of 1000 parlays, Account Balance: {bankroll2}')
    else:
        print(f'It took {bankrupt} parlays to go bankrupt')

hitPercentage = input("Roughly what percentage of your bets do you hit: ")
legs = input("How many legs are each parlay that you place (2-5) : ")
bankroll = input("Enter how much money you are starting with: ")
wager = input("Enter how much you wager per bet: ")

TrialSet(legs, hitPercentage, bankroll, wager)

