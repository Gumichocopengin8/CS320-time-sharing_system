# CS320 Time Sharing System

## Project1
### Description 
#### Problem:  
To create a simple time-sharing system.  To use the time-sharing system to “play” with the time slices to find the most efficient turnaround times using a round-robin selection algorithm.  To see what happens using time slices of varying lengths.  To allow the flexibility to build upon this time-sharing system for future projects.ffffffffffffff

Analysis:  A simple time sharing system will need several features:
-	A processor (or simulation of placing a process on the processor)
-	A waiting queue for jobs waiting for the processor
-	A selection algorithm for choosing which process gets the processor next
-	A clock with which to measure time slices
-	An Audit log to record job starting and ending times of processes

#### Design/Assumptions:
These are some of the things that you may want to track in your processes.  Keep your design flexible so more items can be added later.
-	Job Number or other identification
-	Total CPU time needed to complete
-	Total CPU time completed
-	Maybe time entered onto the queue, time started on CPU, time spent waiting, and time completed.

Other design assumptions include:
-	You may use any language, on any platform of your choosing.
-	You will work in teams of 3/4, so we should have 2 teams of 4 and one of 3.
-	Processes will be loaded into the system all at once using an input file of your design.
-	You choose the number of processes to load and their running times.
-	All processes have equal priority.
-	A process running on the CPU is simply one that is pointed to by the process index and gets the processor for the amount of the time slice.
-	All processes are entirely CPU-bound.  We will not yet add interrupts for I/O.
-	You may make a fixed assumption for context switching time.
-	Assume all processes fit into main memory.  Ignore all other memory issues.
-	The clock that you use to measure time slices may be the system clock or a simple counter.
-	You will need to account for context switching time.  Every time you swap jobs on the processor, it takes a very small amount of time to save the running programs context, run the dispatcher, and restore the new processes context before it can begin running.
-	Make your selection algorithm such that it will be easy to pull out and insert a different algorithm in the future.
-	Your audit log may be a screen shot or a report.  It may be written to as processes begin and end or it may be a report done when all processes have completed.  A report upon completion may be the easiest to read and a timeline could be reconstructed.

#### Deliverables:
Upon completion, please submit the following through Moodle.  This project is worth a total of 45 points.
-	Your program(s), including proper documentation for your program. In addition to documenting the code, you should have a separate design document which also includes information on building and running your simulation.  (20 points)
-	Your input file and input file format (5 points)
-	Your final audit log(s) (10 points)
-	A lab write-up containing the results that you have found and your conclusions (10 points)
-	During a lab period following the due date, you may be asked to provide a demonstration of your simulator in action and describe your design and results.

---
`Project2 is skipped because of no time in class`

---

## Project3
### Description  
Short-Term Scheduling Simulation

Objective:  To calculate Turnaround and Normalized Turnaround Times for our systems as they exist and to compare those with another selection algorithm of our choosing.

#### Problem: 
a) To modify your simple time-sharing simulation with priority to calculate and display the final turnaround times and normalized turnaround times for each process in the final output log.  Get some statistics using what you found as your “best” time quantum from project 0.  Get a set of data using all equal priorities and a set of data with some different priorities.  

b)  Modify your system again to implement one of the other scheduling algorithms of your choosing (SRT, SPN, HRRN, or FB).  Do not use Round-Robin or FCFS.  

c) Analyze the turnaround data collected on all three runs and report what you have found.  Create some graphs comparing the runs to each other (i.e. in Excel).  


#### Deliverables:
Upon completion, please submit the following items.  This project is worth a total of 35 points.
-	A copy of your new program, including the new scheduling algorithm (10 points)
-	Your log files for your round-robin system (differing priorities and equal priorities), including turnaround data (5 points)
-	Your log file using your new selection algorithm, including turnaround data (5 points)
-	An analysis of your data and comparison of your simulations (15 points)

## Python Version
- Python 3.6.0^
