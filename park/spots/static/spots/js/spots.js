$(document).ready(function() {
	$('#address-input').change(submitForm);
	$('#from-date').change(submitForm);
	$('#from-time').change(submitForm);
	$('#to-date').change(submitForm);
	$('#to-time').change(submitForm);

	function submitForm() {
		$('form')[0].submit();
	}
});