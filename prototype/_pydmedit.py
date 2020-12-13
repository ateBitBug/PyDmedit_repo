'''*
  demo edit pseudo code
  - prepare an input data file to edit (a csv file with the header variables)
  - a user creates a file which lists out the variables need for an edit
    -> the list of these variables are a subset of the prepared input data file
      -> these variables must come from the csv file's header variables
          -> the variables can be all of the header variables or some of them
        -> when making this var list file, it must include "key" variables which
          can uniquely identify each row.  There cannot be rows with duplicate
          keys
        -> call this list of variables file
          -> edit.var
            -> if the csv file would look as follows:
              var1, var2, var3, var4, var5
                a,    b,    c,    d,    e
                f,    g,    h,    i,    j
            
              the 'edit.var' file could have a list of variables such as:
                var2
                var1
                var4

              *the order of the variables doesn't matter; furthermore, new
              variables (not listed in the csv header) can be added in
              'edit.var' so that these new variables are available to store
              new data.  these new variables are added in any order such as:
                newvar1
                var2
                newvar3
                var1
                var4
                newvar2

                NOTE: these new variables will be initialized to 'blank'

  - 'edit.var' file is used in two different ways:
    - the variables listed in 'edit.var' are used to subset the csv input data
      file; it is used to create an output with the same number of records but
      with less variables.
    - 'edit.var' is used to create a class of variable objects which act as
      containers which store the variables and their respective values
        -> these class definitions are created by a python script based on the
          variables shown in 'edit.var'

  - the subset of the main csv input data files are sorted by the user defined
    key variables
      -> if a subset file were to have duplicate key rows, these duplicate rows
        can be removed by the sort routine

    - does it need to subset by several variables?
      -> yes
        -> make a list of variables to subset from the csv header
      -> no
        -> use the entire variables in the csv header
  - a list of variables to keep from the original input data file
    -> read the csv input data file (including the header line)
      -> for each line of the input data file, extract the columns of the
        variables along with their respective values
        -> output these column values to a file
*'''