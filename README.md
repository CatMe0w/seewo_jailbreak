# seewo_jailbreak

Defuse Seewo's PASSWORDV3/LockPasswordV3

解除希沃 PASSWORDV3/LockPasswordV3 管理员密码

Tested on SeewoService 1.5.1.3728 and 1.5.1.3730.

已在希沃管家 1.5.1.3728 和 1.5.1.3730 上测试通过。

## Usage

1. Download `seewo_jailbreak.exe` from [Releases](https://github.com/CatMe0w/seewo_jailbreak/releases).  
(Or download `seewo_jailbreak.py` if you have Python installed.)  

2. Copy `bind_zmodule.dll` from `C:\Program Files (x86)\Seewo\SeewoService\SeewoService_1.X.X.XXXX\SeewoCore\module\bind\` to the same directory as `seewo_jailbreak.exe`.
   
3. Run `seewo_jailbreak.exe` to generate the patched file.
   
4. Replace `C:\Program Files (x86)\Seewo\SeewoService\SeewoService_1.X.X.XXXX\SeewoCore\module\bind\bind_zmodule.dll` with the patched file.

5. Restart the computer.

6. Now you can pass the admin password with any password.

> [!NOTE]  
> 
> You may need to kill `SeewoCore.exe` and `SeewoFreezeUpdateAssist.exe` processes first.
> 
> If it doesn't work, even if you have killed the process, please restart to Safe Mode and try again.

---

1. 从 [Releases](https://github.com/CatMe0w/seewo_jailbreak/releases) 下载 `seewo_jailbreak.exe`。  
（或者如果你已经安装了 Python，可以下载 `seewo_jailbreak.py`。）

2. 从 `C:\Program Files (x86)\Seewo\SeewoService\SeewoService_1.X.X.XXXX\SeewoCore\module\bind\` 复制 `bind_zmodule.dll` 到 `seewo_jailbreak.exe` 同一目录下。

3. 运行 `seewo_jailbreak.exe` 修补文件。

4. 用修补后的文件替换 `C:\Program Files (x86)\Seewo\SeewoService\SeewoService_1.X.X.XXXX\SeewoCore\module\bind\bind_zmodule.dll`。

5. 重启电脑。

5. 现在你应该已经可以用任意密码通过管理员密码验证。

> [!NOTE]
>
> 你可能需要先结束 `SeewoCore.exe` 和 `SeewoFreezeUpdateAssist.exe` 进程。
>
> 如果你已经结束了进程，但仍然无法覆盖文件，请重启到安全模式重试。

## License

MIT License
