# define the function for the lab using `def`
def lab_1():
  # Have the user enter the number of scores they need to submit
  num_scores = int(input("Enter the number of scores: "))
  # Create an empty list to store the scores
  scores_list = []
  # Use a loop to populate the scores list
  for i in range(num_scores):
    # cast the score to a quantitative value
    score = float(input(f"Enter score number {i+1}: "))
    scores_list.append(score)
  # Validate that the scores list has values
  print(scores_list)
  # Calculate the average score using list comprehension (list functions)
  avg_score = sum(scores_list)/len(scores_list)
  # Use elifs to assess the range and come up with the letter grade
  if avg_score >= 90:
    print("A", avg_score)
  elif avg_score >= 80 and avg_score < 90:
    print("B", avg_score)
    ### Add the missing conditions here
  else:
    print("F", avg_score)

# You must invoke the function for the logic to execute
lab_1()                 
