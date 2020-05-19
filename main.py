import sys, database

for arg in range(1, len(sys.argv)):

    # Read in file name from cmd line
    input_file = sys.argv[arg]
    with open(input_file, "r") as read_file:
 
        transaction_count = 0   # Used to know whether inside of a transaction
        records = []   # Transaction Blocks
        prev = []   # Keeps track of prev variable to maintain ROLLBACK consistency
        my_db = database.Database() # Database

        # The following will Parse and Execute Commands
        for line in read_file:
            
            # Separate Command Arguments into a list
            # and assign to simpler variables for Readability

            arguments = line.split()
            length = len(arguments)
            COMMAND = arguments[0]
            if length == 2:
                name = arguments[1]
            if length == 3:
                name = arguments[1]
                value = arguments[2]

            # The Interface for DataBase Commands

            # BEGIN: Starts Transaction
            # Instantiate Block via empty array in records[]. This will contain the 'history' of commands.
            # Keep track if we are in a transaction block when greater than 0.
            if COMMAND == 'BEGIN': 
                records.append([])
                transaction_count += 1

            # Update database with new value
            # In a transaction block previous value overwritten stored in prev[]
            # a hashtag placeholder maintains that no previous value existed
            # record appropriate log to record
            if COMMAND == 'SET':
                if transaction_count > 0:
                    if len(prev) > 0:
                        log = 'SET ' + name + ' ' + str(value) + ' ' + str(prev.pop())
                    else:
                        log = 'SET ' + name + ' ' + str(value) + ' ' + '#' # first execution of 'SET' Command
                    records[-1].append(log) # Adds record to the last log in records[]
                my_db.SET(name, value)
                prev.append(value)
            
            # Remove value from Database
            # In a transaction store log appropriately
            if COMMAND == 'UNSET':
                my_db.UNSET(name)
                if transaction_count > 0:
                    log = 'UNSET ' + name + ' ' + str(value)
                    records[-1].append(log) # Add record to the last log in records[]

            
            # ROLLBACK: UNDO everything within most recent transaction block.
            # Decrement the 'tracker' variable, to know when a transaction is finished.
            if COMMAND == 'ROLLBACK':
                transaction_count -= 1

                # No COMMANDS have occured hence empty "Block history", records[] 
                if len(records) == 0:
                    print('NO TRANSACTION')
                
                else:
                    # Parse the "Block history" of last inputted transaction Block
                    # and "undo" commands while maintaining previous values
                    for record in records[-1]:
                        log = record.split()
                        if log[0] == 'SET' and log[3] == '#': # Hashtag is a place holder if prev[] is empty.
                            my_db.UNSET(log[1])
                        elif log[0] == 'UNSET':
                            my_db.SET(log[1],int(log[2]))
                        else:
                            my_db.SET(log[1], int(log[3]))
                    records.pop()

            # Resets transaction counter and "Block history" -> records[]
            if COMMAND == 'COMMIT':
                if len(records) == 0:
                    print('NO TRANSACTION')
                else:
                    transaction_count = 0
                    records = []

            # Counts all keys with same Value
            if COMMAND == 'NUMWITHVALUE':
                my_db.NUMWITHVALUE(arguments[1])
            
            # Prints Value of 'name'
            if COMMAND == 'GET':
                my_db.GET(name)

            # deletes db and sends exception to quit python interpreter.
            if COMMAND == 'END':
                del my_db
                SystemExit()