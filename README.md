# bester-linux
best-linux.cs.wisc.edu is supposed to redirect to the machine with the lowest load.
This usually is not the case and seems to just pick a machine at random.

Currently `machines.txt` has a list of the linux machines.
Each machine has a file `/proc/stat` which has [this format](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk65143).
For bonus points factor in memory usage into the heuristic for best machine.