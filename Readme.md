# perceptron
 - 程式執行說明
    1.  輸入檔案路徑(有path.txt 上有路徑可以複製貼上)、learning_rate、epoch、accuracy![](https://i.imgur.com/mozeE1Z.png)
    2. 如果找不到檔案 就會出現 input->1 continue, input->2 stop，輸入1可以繼續 輸入2就會停止    
    ![](https://i.imgur.com/9ivLBzq.png)
    3. 另外如果learning_rate, epoch, accuracy輸入錯誤需要重新輸入  
        ![](https://i.imgur.com/1YnralB.png)    
    4. 輸入都正確就會開始執行，每個epoch都會輸出train的accuracy, test的accuracy, total_data的accuracy ![](https://i.imgur.com/OOunjvu.png)
    5. 訓練完之後會跑出第一張圖，使用train_data下的資料與weight畫出來的(比較train_data與訓練結果的關係)
        ![](https://i.imgur.com/AAmBy0p.png)
    6. 關掉圖片後，就會出現最後的結果，包刮:total_accuracy, wieght, all data accuracy
        ![](https://i.imgur.com/2HGKWlO.png)
    7. 出現all data與weight的圖
        ![](https://i.imgur.com/cKvDOaG.png)
    8. 出現的圖檔會存在dataset/image/，如果找不到目錄會出現以下圖片，不影響程式執行。
        ![](https://i.imgur.com/wuBaUUm.png)

