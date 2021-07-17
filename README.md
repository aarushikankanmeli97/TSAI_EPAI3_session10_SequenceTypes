# TSAI_EPAI3_session10_SequenceTypes

# Project Description:

    This repository contains Assignemnt for session 10 on SequenceTypes.

# Sequence Types : 

    In Python programming, sequences are a generic term for an ordered set which means that the order in which we input the items will be the same when we access them.
    Python supports six different types of sequences. These are strings, lists, tuples, byte sequences, byte arrays, and range objects.

# Detailed explanation of Objective1 :

    - Start with necessay imports.
    - Create polygon class that takes num edges/vertices and circumRadius as input attributes.
    - This class provides following properties:
        1. # edges = n
        2. # vertices = R
        3. interior angle = (n−2)⋅180/n
        4. edge length = 2⋅R⋅sin(π/n)
        5. apothem = R⋅cos(π/n)
        6. area = 1/2⋅n⋅s⋅a
        7. perimeter = n⋅s
    - __repr__ function represents the class's objects as a string.
    - __eq__ function represents the equality function on both edges/vertices and circumRadius.
    - __gt__ function represents the greater than function on edges/vertices only.

# Detailed explanation of Objective2 :

    - Start with necessary imports along with Objective1 module.
    - Create polygon sequence class that takes num edges/vertices and circumRadius as input attributes.
    - Checks if the passed number of edges or vertices are less than 3, if so, raises an exception as the smallest polygon has minimum of 3 sides.
    - The list comprehension arranges the polygon in the ascending order based on the number of edges defines by the user.
    - Max_Eff_Pol() function is used to calculate the maximum effeciency of polygon based on highest area:perimeter ratio.

# Table of contents :
- TSAI_EPAI3_session10_SequenceTypes
	- .github
		- workflow
			- ci.yml
	-.gitignore
	-requirements.txt
	-Objetive1.py
    -Objetive2.py
	-test_session0.py