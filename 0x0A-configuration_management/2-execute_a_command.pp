exec { 'killmenow':
# create a manifest that kills a process named killmenow
  command => 'pkill'
}
