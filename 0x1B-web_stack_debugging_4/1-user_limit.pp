# Change file descriptor limits
exec { 'set soft limit to 2000':
  path    => '/bin',
  command => "sed -i 's/4/2000/' /etc/security/limits.conf"
}

exec { 'set hard limit to 2000':
  path    => '/bin',
  command => "sed -i 's/5/2000/' /etc/security/limits.conf"
}
