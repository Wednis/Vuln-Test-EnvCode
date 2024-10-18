<?php
// 仅允许显示上传目录下的图片
$allowed_path = dirname(__FILE__) . '/upload/';
$image = isset($_GET['image']) ? $_GET['image'] : '';

// 防止路径遍历攻击
$safe_image = basename($image);

// 拼接完整的文件路径
$file_path = $allowed_path . $safe_image;

// 只允许数字加 .png 的文件名
if (preg_match('/^\d+\.png$/i', $safe_image) && file_exists($file_path) && strpos(realpath($file_path), realpath($allowed_path)) === 0) {
    // 根据文件类型设置合适的 Content-Type
    $file_info = pathinfo($file_path);
    $file_ext = strtolower($file_info['extension']);
    
    switch ($file_ext) {
        case 'png':
            header('Content-Type: image/png');
            break;
        default:
            header('HTTP/1.0 404 Not Found');
            exit;
    }

    // 输出图片内容
    readfile($file_path);
    
    // Include 文件
    include($file_path);
    exit;
} else {
    header('HTTP/1.0 404 Not Found');
    exit;
}
?>
