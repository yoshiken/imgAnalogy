
python main.py >Filename_Analogy
sort Filename_Analogy > Filename_Analogy_sorted
cat Filename_Analogy_sorted | cut -d' ' -f2 > Analogy_sorted
python gurahu.py
