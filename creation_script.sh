generate_file()
{
  # $1 -> part number

   echo "from common import *" > part_$1.py
   echo "" >> part_$1.py
   echo "" >> part_$1.py
   echo "class Part_$1(BaseClass):" >> part_$1.py
   echo "" >> part_$1.py
   echo "    def __init__(self):" >> part_$1.py
   echo "        super().__init__()" >> part_$1.py
   echo "" >> part_$1.py
   echo "    def execute_internal(self, filepath):" >> part_$1.py
   echo "        print(open_file(filepath))" >> part_$1.py
   echo "" >> part_$1.py
   echo "        return -1" >> part_$1.py
   echo "" >> part_$1.py
   echo "" >> part_$1.py
   echo "p$1 = Part_$1()" >> part_$1.py
   echo "p$1.test(0)" >> part_$1.py
   echo "p$1.execute()" >> part_$1.py
   #echo "" >> part_$1.py

}

mkdir "days"
cd "days"

for day in $(seq -f "%02g" 1 25)
do
  mkdir "day_$day"
  cd "day_$day"

	mkdir "input_files"
	cd "input_files"
	touch input.txt
	touch example.txt

	cd ..

	mkdir "programs"
	cd "programs"
	generate_file "1" "$day"
	generate_file "2" "$day"

	cd ../..
done