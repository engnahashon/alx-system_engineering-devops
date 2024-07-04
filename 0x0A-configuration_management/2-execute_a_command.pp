exec { 'killmenow':
# create a manifest that kills a process named killmenow
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}
