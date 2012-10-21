#!/usr/bin/env ruby
# coding: utf-8

require "sosowa"
require "pp"

indexes = []
s = Sosowa.get :log => 127
127.times do |n|
  puts "fetch #{n}"
  indexes << s.to_a
  s = s.next
end
indexes.flatten!
pp indexes.size

indexes.each do |index|
  cnt = 0
  begin
    novel = index.fetch
  rescue => e
    cnt += 1
    next if cnt < 4
    puts "# Retry..."
    retry
  end
  puts novel.entry.title
  open("data/sosowa-#{novel.entry.id}.txt", "w").write(novel.plain)
  open("data/sosowa-all.txt", "a+").write(novel.plain)
end