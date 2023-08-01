#!/usr/bin/env ruby
# only scans capital letters

puts ARGV[0].scan(/[A-Z]*/).join
