import time
import random
# Read file and save entries to map
def convert_file_to_map(file_path):
    try:
        with open(file_path,'r') as file:
            # Save contents to map
            animal_map = dict()
            lines = file.readlines()

            for line in lines:
                data = line.split(',')
                animal,question = data[0],data[1].rstrip('\n')
                animal_map[animal] = question
            file.close()
            return animal_map
    except (FileNotFoundError,IOError):
        print('Error with reading file')

# Write elements in list to file
def write_file(file_path,save_list_map):
    try:
        with open(file_path,'w') as write_file:
            write_file.writelines(save_list_map)
            write_file.close()
    except (FileNotFoundError,IOError):
        print('Error with writing file')

# Capture input, return True or False
def capture_boolean_input(msg):
    print(msg)
    value = input('Input: ') 
    value = value.strip().lower() 
    if value == 'no':
        return False
    if value == 'yes':
        return True
    print('We only accept a yes or no:')
    return capture_boolean_input()

# Main app
def main(): 
    file_path = './database/animals.txt'
    animal_map = convert_file_to_map(file_path)

    # Into
    print('Think of an Animal, I will ask you some questions and tell you what animal it is. You have 5 seconds')
    time.sleep(5)
    
    default_answer = 'dog'
    cpu_guess = 'is it a: '
    player_guess = False
    play_again = True
    num_of_guesses = 0
    
    animal_guess_array = list(animal_map.keys())
    # if map empty, start first guess
    if len(animal_map) == 0:
       player_guess = capture_boolean_input(cpu_guess + default_answer)

    # loop to keep playing
    while play_again:
        # Add question if initial guess correct
        if num_of_guesses == 0:
            animal = 'tiger'
            diff = 'stripes'
            animal_map[animal] = diff
            animal_guess_array.append(animal)
            play_again = capture_boolean_input("Play again? ")
            num_of_guesses+=1
            continue
        if len(animal_map) > 0:
            # Cpu guesses
            random_guess = random.choice(animal_guess_array)
            question = 'Does your animal have '+ animal_map[random_guess]+"?"
            player_guess = capture_boolean_input(question)
            if player_guess:
                print(cpu_guess+ random_guess)
            
        # If player guess false, ask user what is animal, what is difference between last answer and Your animal, add question to map
        if player_guess == False:
            capture_animal = input("What is your animal? ").strip().lower() 
            capture_diff = input("What is the difference between last answer and your animal? ").strip().lower() 
            animal_map[capture_animal] = capture_diff
            animal_guess_array.append(capture_animal)
        play_again = capture_boolean_input("Play again? ")
    
    # Save map items to list
    save_list_Map = [animal+','+animal_map[animal]+'\n' for animal in animal_guess_array]
    
    write_file(file_path,save_list_Map)
 
main()
