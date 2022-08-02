if(isset($_GET['FeedbackForm'])){
    $mailtext = '';
    $mailtext .='F.I.SH:<b>'.$_GET['FeedbackForm']['name'].'</b><br/>';
    $mailtext .='Yuridik shaxs nomi (Tadbirkor):<b>'.$_GET['FeedbackForm']['userpassword'].'</b><br/>';
    $mailtext .='Elektron manzil:<b>'.$_GET['FeedbackForm']['email'].'</b><br/>';
    $mailtext .='Telafon raqam:<b>'.$_GET['FeedbackForm']['phone'].'</b><br/>';
    $mailtext .='SHahar:<b>'.$_GET['FeedbackForm']['city'].'</b><br/>';
    $mailtext .='Viloyat:<b>'.$_GET['FeedbackForm']['region'].'</b><br/>';
    $mailtext .='Manzil:<b>'.$_GET['FeedbackForm']['address'].'</b><br/>';
    $mailtext .='Mavzu:<b>'.$_GET['FeedbackForm']['subect'].'</b><br/>';
    $mailtext .='Jins:<b>'.$_GET['FeedbackForm']['sex'].'</b><br/>';
    $mailtext .='Tugilgan sana:<b>'.$_GET['FeedbackForm']['born'].'</b><br/>';
    $mailtext .='status:<b>'.$_GET['FeedbackForm']['status'].'</b><br/>';
    $mailtext .='handling:<b>'.$_GET['FeedbackForm']['handling'].'</b><br/>';
    $mailtext .='Murojaatnoma:<b>'.$_GET['FeedbackForm']['body'].'</b><br/>';
  Yii::$app->mailer->compose()
        ->setFrom('toshvilu@toshvil.uz')
        ->setTo('antikorrupsiya@toshvil.uz')
        ->setSubject('Email')
        ->setTextBody('Plain text content')
        ->setHtmlBody($mailtext)
        ->send();
/*    $from = "noreply@toshvil.uz";
    $headers = "From:" . $from;
    echo mail ("Biloliddin@bk.ru" ,"testmailfunction" , "Oj",$headers);*/
    echo $mailtext;
    
    echo '<h2>Email muofaqiyatli yuborildi</h2>';

}

if(isset($_POST['FeedbackForm'])){
    $mailtext = '';
    $mailtext .='F.I.SH:<b>'.$_POST['FeedbackForm']['name'].'</b><br/>';
    $mailtext .='Yuridik shaxs nomi (Tadbirkor):<b>'.$_POST['FeedbackForm']['userpassword'].'</b><br/>';
    $mailtext .='Elektron manzil:<b>'.$_POST['FeedbackForm']['email'].'</b><br/>';
    $mailtext .='Telafon raqam:<b>'.$_POST['FeedbackForm']['phone'].'</b><br/>';
    $mailtext .='SHahar:<b>'.$_POST['FeedbackForm']['city'].'</b><br/>';
    $mailtext .='Viloyat:<b>'.$_POST['FeedbackForm']['region'].'</b><br/>';
    $mailtext .='Manzil:<b>'.$_POST['FeedbackForm']['address'].'</b><br/>';
    $mailtext .='Mavzu:<b>'.$_POST['FeedbackForm']['subect'].'</b><br/>';
    $mailtext .='Jins:<b>'.$_POST['FeedbackForm']['sex'].'</b><br/>';
    $mailtext .='Tugilgan sana:<b>'.$_POST['FeedbackForm']['born'].'</b><br/>';
    $mailtext .='status:<b>'.$_POST['FeedbackForm']['status'].'</b><br/>';
    $mailtext .='handling:<b>'.$_POST['FeedbackForm']['handling'].'</b><br/>';
    $mailtext .='Murojaatnoma:<b>'.$_POST['FeedbackForm']['body'].'</b><br/>';
  Yii::$app->mailer->compose()
        ->setFrom('toshvilu@toshvil.uz')
        ->setTo('antikorrupsiya@toshvil.uz')
        ->setSubject('Email')
        ->setTextBody('Plain text content')
        ->setHtmlBody($mailtext)
        ->send();
/*    $from = "noreply@toshvil.uz";
    $headers = "From:" . $from;
    echo mail ("Biloliddin@bk.ru" ,"testmailfunction" , "Oj",$headers);*/
    echo $mailtext;
    $toEmail = 'antikorrupsiya@toshvil.uz'
    if(mail($toEmail, 'xabar', $mailtext)){
        echo '<h2>Email muofaqiyatli yuborildi</h2>';
    }

}
