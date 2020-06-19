import ansible_runner

r = ansible_runner.run(host_pattern='all', module='command', module_args='ls')
print("{}: {}".format(r.status, r.rc))
# successful: 0
for each_host_event in r.events:
    print(each_host_event['event'])
print("Final status:")
print(r.stats)