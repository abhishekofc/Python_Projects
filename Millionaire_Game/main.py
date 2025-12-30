questions =[
    ["Who is Shah Rukh Khan?","WWE Wrestler","Prime Minister of India","Cricketer","Actor",4],
    ["What is the capital of India?","Mumbai","Chennai","New Delhi","Kolkata",3],
    ["Which planet is known as the Red Planet?","Earth","Mars","Jupiter","Saturn",2],
    ["What is the largest mammal in the world?","Elephant","Blue Whale","Giraffe","Great White Shark",2],
    ["Who wrote 'Romeo and Juliet'?","Charles Dickens","William Shakespeare","Mark Twain","Jane Austen",2],
    ["Which element has the chemical symbol 'O'?","Gold","Oxygen","Silver","Hydrogen",2],
    ["What is the hardest natural substance on Earth?","Gold","Iron","Diamond","Platinum",3],
    ["Who painted the Mona Lisa?","Vincent van Gogh","Pablo Picasso","Leonardo da Vinci","Claude Monet",3],
    ["What is the smallest prime number?","0","1","2","3",3],
    ["Which ocean is the largest?","Atlantic Ocean","Indian Ocean","Arctic Ocean","Pacific Ocean",4]
]

prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

i=0
for question in questions:
    
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}") 

    # Check whether the answer is correct or Not ?
    answer = int(input("Enter your anser. 1 for a, 2 for b, 3 for c, 4 for d: "))
    if(question[5] == answer):
        print("Congratulations! Your answer is correct.\n")
    else:
        print(f"Sorry! Correct answer is {question[5]}.\n")
        print("Game Over!")
        break;
    print(f"You have won Rs. {prizes[i]}\n")
    i+=1