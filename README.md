[![CircleCI](https://circleci.com/gh/jumaxbrian/jumo_aggregate.svg?style=svg)](https://circleci.com/gh/jumaxbrian/jumo_aggregate)

# Accounting Aggreagate

1. ### Project
    1. This project mainly processes a CSV from our accounting department and calculate the aggregate loans by the tuple of (Network, Product, Month) with the total currency amounts and counts and output into a file CSV file called Output.csv

1. ### Assumptions
    1. The MSISDNs are unique and thus no duplicates exist in the Loans.csv file
    1. Each of the entries contains exactly 5 fields and that the program doesn't necessarily need to provide the entreis that do not meet these requirements. It only selects the ones that meet those requirements and then processes them.
    1. The timeseries aspect of the data was important, therefore, the grouping considered the months as month-year. For instance, 16-Mar-2016 and 16-Mar-2017 will not be aggregated because their months will be considered as Mar-2016 and Mar-2017 respectively.
    1. Program will run on a unix-like environment.

1. ### Performance and Scaling considerations
    1. The program attempted to emulate a map-reduce paradigm in order to allow for horizontal scaling. The map part consists of the files `cat`,`accept_only_five_columns.sh` and `mapper.py`. Then, we sort the results to limit the memory usage in the reducer with the program `sort_loans.sh` and finally perform the reduction using the file `reducer.py`.

    1. Bash and Python3 were used in coming up with this program. Bash was used because of the toolsets it has e.g. awk that enable fast processing of data especially in streams. The sort program was also used to perform fast sorting. Python was mainly used to allow for Object Oriented Programming style and also due to the fact that it's a more readable scripting language with many libraries for additional functions.

    1. Input and output streams have been used to reduce the memory requirements of reading an entire file before processing. This usually results in faster programs that can handle data larger than the memory of the given machine before resorting to virtual memory.

1. ### Usage
    1. Ensure you have Python3 and Bash environments in your local machine
    1. Clone this repository to your local machine
    1. Move into the directory i.e. `jumo_aggregate` if you used the default one.
    1. run the main program like this `./main.sh`
    1. You will get a prompt to input the filename
    1. If the file exists and is not empty, the data will be processed and you will find the results in the Output.csv file
    1. If there are errors during the reading of the file, they will be shown on your standard output
    1. Errors during the data processing are logged into the file app.log