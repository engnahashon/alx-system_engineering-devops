package { 'flask':
# Install the flask package using pip3
  ensure   => '2.1.0'
  provider => 'pip3'
}
