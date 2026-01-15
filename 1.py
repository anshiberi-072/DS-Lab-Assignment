"""
ALGORITHM: Arrange_Almirah

INPUT: n (number of shelves), Pile_of_Clothes (unsorted)

Step 1: Categorization
   - Iterate through Pile_of_Clothes.
   - Separate items into three groups: 
     a. Formals (Office wear)
     b. Casuals (Home wear)
     c. Occasionals (Traditional/Party)

Step 2: Assign Priority (Frequency Logic)
   - Identify 'Eye-Level' shelves (usually n/2).
   - Identify 'Hard-to-reach' shelves (Top and Bottom).

Step 3: Placement Loop
   - Place 'Formals' on 'Eye-Level' shelves for quickest retrieval (Minimizing time).
   - Place 'Casuals' on shelves immediately below Eye-Level.
   - Place 'Occasionals' on the highest or lowest shelves.

Step 4: Optimization within Shelf
   - For T-shirts and Jeans: Fold and Stack vertically.
   - For Ironed Shirts: Use hanging space if available, else fold flat.
   
Step 5: End
"""