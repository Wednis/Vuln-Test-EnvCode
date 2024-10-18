<?php
header("Content-type: text/html;charset=utf-8");
error_reporting(0);

// 设置上传目录
define("UPLOAD_PATH", dirname(__FILE__) . "/upload/");
define("UPLOAD_URL_PATH", str_replace($_SERVER['DOCUMENT_ROOT'], "", UPLOAD_PATH));

if (!file_exists(UPLOAD_PATH)) {
    mkdir(UPLOAD_PATH, 0755);  // 创建上传目录
}

$is_upload = false;

if (!empty($_POST['submit'])) {
    $name = basename($_FILES['file']['name']);
    $filetype = $_FILES['file']['type'];
    $fileext = pathinfo($name)['extension'];
    $tmpname = $_FILES['file']['tmp_name'];
    $upload_file = UPLOAD_PATH . '/' . $name;

    // 只允许上传 png 文件
    if (($fileext == "png") && ($filetype == "image/png")) {
        if (move_uploaded_file($tmpname, $upload_file)) {
            // 使用上传的图片生成新的图片
            $im = imagecreatefrompng($upload_file);

            if ($im == false) {
                echo "文件检查失败，只允许传png文件。";
                @unlink($upload_file);
            } else {
                // 给新图片指定文件名
                srand(time());
                $newfilename = strval(rand()) . ".png";

                // 保存新图片到指定目录
                $img_path = UPLOAD_PATH . '/' . $newfilename;
                imagepng($im, $img_path);
                @unlink($upload_file);
                $is_upload = true;

                echo "文件上传成功，已保存为：<a href='view.php?image=" . UPLOAD_URL_PATH . $newfilename . "'>" . $newfilename . "</a>";
            }
        } else {
            echo "文件上传失败。";
        }
    } else {
        echo "只允许上传 png 文件。";
    }
}
?>
