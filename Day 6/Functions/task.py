# Challenge 1 to make square in Reeborg's world
#     link:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#     Code:
#     '''
#     def turn_right():
#         turn_left()
#         turn_left()
#         turn_left()
#
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     '''
#
# Challenge 2: Hurdle 1
#     link:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#     Code:
#     '''
#     def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#     def hurdle():
#         move()
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#
#     for i in range(6):
#         hurdle()
#     '''
#
# Challenge 3: Hurdle 2(Learnt using While loops)
#     link:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
#     Code:
#     '''
#     def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#     def hurdle():
#         move()
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#
#     while at_goal() == False:
#         hurdle()
#     '''
#
# Challenge 4: Hurdle 3
#     link:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
#     Code:
#     '''
#     def turn_right():
#         turn_left()
#         turn_left()
#         turn_left()
#
#     def hurdle():
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#
#     while at_goal() == False:
#         if wall_in_front():
#             hurdle()
#         else:
#             move()
#     '''
#
# Challenge 5: Hurdle 4
#     link:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#     Code:
#     '''
#     def turn_right():
#         turn_left()
#         turn_left()
#         turn_left()
#
#     def hurdle():
#         turn_left()
#         while right_is_clear() != True:
#             move()
#         turn_right()
#         move()
#         turn_right()
#         while wall_in_front() != True:
#             move()
#         turn_left()
#
#     while at_goal() == False:
#         if wall_in_front():
#             hurdle()
#         else:
#             move()
#     '''
#
# Final Project: Escaping the Maze
#     link:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#     Code:
#     '''
#     def turn_right():
#         turn_left()
#         turn_left()
#         turn_left()
#
#     while front_is_clear():
#         move()
#     turn_left()
#
#     while not at_goal():
#         if right_is_clear():
#             turn_right()
#             move()
#         else:
#             turn_left()
#     '''