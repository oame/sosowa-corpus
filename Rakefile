#!/usr/bin/env rake

require "sosowa"

namespace :corpus do
  desc "Fetch all of novels from Sosowa"
  task :fetch do
    Dir.mkdir("data") unless FileTest.exists? "data"
    Dir.mkdir("data/novels") unless FileTest.exists? "data/novels"

    indexes = []
    s = Sosowa.get
    begin
      puts "Indexing subject of #{s.log}"
      indexes << s.to_a
    end while s = s.next
    indexes.flatten!
    puts "Indexed #{indexes.size} novels"

    curr = 0
    indexes.each do |index|
      curr += 1
      print "(#{curr}/#{indexes.size}) Fetching #{index.title} ... \t"
      cnt = 0
      begin
        novel = index.fetch
      rescue => e
        cnt += 1
        next if cnt < 4
        puts " Error, Retrying #{cnt} count"
        retry
      end
      open("data/novels/sosowa-#{novel.entry.id}.txt", "w").write(novel.plain)
      puts "Done"
    end
  end

  desc "Unify part of novels"
  task :unify do
    paths = Dir.glob("data/novels/sosowa-*.txt")
    paths.each do |path|
      puts "Appending #{File.basename(path)} to sosowa-all.txt"
      open("data/sosowa-all-plain.txt", "a+").write(open(path).read)
    end
  end
end