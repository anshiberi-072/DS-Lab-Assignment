"""
ALGORITHM: Pack_Suitcase

INPUT: Trip_Duration (7 days), Activity_List, Suitcase_Capacity

Step 1: Selection (Filtering)
   - For each Day in Trip_Duration:
       - Check Activity_List (e.g., Hiking, Dinner).
       - Select Outfit appropriate for Activity.
   - Add essentials (Toiletries, Undergarments).

Step 2: Layering (Protection & Space Optimization)
   - LAYER 1 (Bottom/Wheels): Place heavy items (Shoes, Denim, Jackets).
     - Logic: Provides stability and doesn't crush other items.
   
   - LAYER 2 (Middle): Roll t-shirts and casual pants.
     - Logic: Rolling saves more space than folding (Space Maximization).
     - Fill gaps in Layer 1 with socks/underwear.

   - LAYER 3 (Top): Fold formal wear/delicate fabrics flat.
     - Logic: Prevents wrinkles (Protection).

Step 3: Accessibility Check
   - Place 'Day 1' pajamas or change of clothes on the very top.
   - Place liquid toiletries in a waterproof bag in an outer pocket.

Step 4: Zip and Weigh
"""
