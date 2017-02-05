<h1>Php model maker</h1>

<p>Usage:</p>
<ul>
	<li> Copy script to your /model directory </li>
	<li> Edit model.pmm configuration file (see example)</li>
	<li> Run script </li>
</ul>

<p>Configuration file example:</p>
<pre>+Contact
email
message</pre>

<p>This will create ClassContact.php with code: </p>

```
<?php
	class Contact
	{
		private $email;
		private $message;

		//setters
		public function set_email($new_email)
		{
			$this->email = $new_email;
		}

		public function set_message($new_message)
		{
			$this->message = $new_message;
		}

		//getters
		public function get_email()
		{
			return $this->email;
		}

		public function get_message()
		{
			return $this->message;
		}
	}
```
