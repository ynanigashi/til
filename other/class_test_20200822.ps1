Class test{
    [String] $hogehoge;

    [Void] show_title([int] $case_no){
        if($case_no -eq 1) {
            Write-Host "";
            Write-host "=================================";
            Write-host "CASE1：直接代入した場合";
            Write-host "=================================";
            Write-Host "";
        }
        elseif ($case_no -eq 2) {
            Write-Host "";
            Write-host "=================================";
            Write-host "CASE2：自動設定のメソッドを利用した場合";
            Write-host "=================================";
            Write-Host "";
        } else {
            throw "値が違う";
        }
    }
}

$test = [test]::new();
$test.show_title(1);
$test.hogehoge = "assignment directory";
$test.hogehoge;

$test.show_title(2);
$test.set_hogehoge("assignment through method");
$test.get_hogehoge();