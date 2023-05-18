#Web stack debuggin 4, change limit
exec { 'change limit to 5000':
  path    => '/bin',
  command => "sed 's/15/5000' /etc/default/nginx"
}

exec { 'restart nginx':
  path    => '/usr/sbin',
  command => 'service nginx restart'
}
