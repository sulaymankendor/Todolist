$(document).ready(function() {
	$('.create-task-btn').on('click', function() {
		$('.form-div').show(500);
		$('.dark').show();
	});
	$('.cancel').on('click', function(event) {
		event.preventDefault();
		$('.form-div').hide(300);
		$('.dark').hide(300);
		$('.task-error-msg').hide()
		$('.description-error-msg').hide()
		$('.task-name').val('')
		$('.description-textarea').val('')
		
	})
	$('.create-btn').on('click', function (event) {
		if ($('.task-name').val() === ''){300
			$('.task-error-msg').show()
		}
		else{
			$('.task-error-msg').hide()
		}
		if ($('.description-textarea').val() === ''){
			$('.description-error-msg').show()

		}
		else{
			$('.description-error-msg').hide()
		}

		if ($('.task-name').val() === '' || $('.description-textarea').val() === '') {
			event.preventDefault();
			
			}
		})
})
