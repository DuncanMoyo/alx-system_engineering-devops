#!/usr/bin/env ruby
# parse one element from the file (not opening the file)

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
