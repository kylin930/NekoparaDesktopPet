import sys
import os
import json
from PyQt6.QtCore import Qt, QTimer, QUrl, QCoreApplication
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QMenu, QDialog,
                             QFormLayout, QDoubleSpinBox, QSpinBox,
                             QPushButton, QSystemTrayIcon, QStyle)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtGui import QCursor, QAction, QIcon

LOCAL_SERVER = "http://127.0.0.1:53421"
CONFIG_FILE = "config.json"

MODEL_LIBRARY = {
    "Azuki (红豆)": {
        "Casual (便服)": {"path": "model/azuki-casual.pure.psb.zip", "config": "azuki-config.js"},
        "Dress (礼服)": {"path": "model/azuki-dress.pure.psb.zip", "config": "azuki-config.js"},
        "Maid (女仆装)": {"path": "model/azuki-maid.pure.psb.zip", "config": "azuki-config.js"},
        "Santa (圣诞装)": {"path": "model/azuki-santa.pure.psb.zip", "config": "azuki-config.js"},
        "Teenage (少女)": {"path": "model/azuki-teenage.pure.psb.zip", "config": "azuki-config.js"},
        "WinterMaid (冬女仆)": {"path": "model/azuki-wintermaid.pure.psb.zip", "config": "azuki-config.js"},
        "Winter (冬装)": {"path": "model/azuki-winter.pure.psb.zip", "config": "azuki-config.js"},
        "Yukata (浴衣)": {"path": "model/azuki-yukata.pure.psb.zip", "config": "azuki-config.js"},
    },
    "Chocola (巧克力)": {
        "Casual (便服)": {"path": "model/chocola-casual.pure.psb.zip", "config": "chocola-config.js"},
        "Dress (礼服)": {"path": "model/chocola-dress.pure.psb.zip", "config": "chocola-config.js"},
        "Koneko (幼年)": {"path": "model/chocola-koneko.pure.psb.zip", "config": "kochocola-config.js"},
        "Lolita (洛丽塔)": {"path": "model/chocola-lolita.pure.psb.zip", "config": "chocola-config.js"},
        "Maid (女仆装)": {"path": "model/chocola-maid.pure.psb.zip", "config": "chocola-config.js"},
        "Pajama (睡衣)": {"path": "model/chocola-pajama.pure.psb.zip", "config": "chocola-config.js"},
        "Santa (圣诞装)": {"path": "model/chocola-santa.pure.psb.zip", "config": "chocola-config.js"},
        "Teenage (少女)": {"path": "model/chocola-teenage.pure.psb.zip", "config": "chocola-config.js"},
        "WinterMaid (冬女仆)": {"path": "model/chocola-wintermaid.pure.psb.zip", "config": "chocola-config.js"},
        "Winter (冬装)": {"path": "model/chocola-winter.pure.psb.zip", "config": "chocola-config.js"},
        "Yukata (浴衣)": {"path": "model/chocola-yukata.pure.psb.zip", "config": "chocola-config.js"},
    },
    "Cinnamon (桂皮)": {
        "Casual (便服)": {"path": "model/cinnamon-casual.pure.psb.zip", "config": "cinnamon-config.js"},
        "Dress (礼服)": {"path": "model/cinnamon-dress.pure.psb.zip", "config": "cinnamon-config.js"},
        "Maid (女仆装)": {"path": "model/cinnamon-maid.pure.psb.zip", "config": "cinnamon-config.js"},
        "Santa (圣诞装)": {"path": "model/cinnamon-santa.pure.psb.zip", "config": "cinnamon-config.js"},
        "Teenage (少女)": {"path": "model/cinnamon-teenage.pure.psb.zip", "config": "cinnamon-config.js"},
        "WinterMaid (冬女仆)": {"path": "model/cinnamon-wintermaid.pure.psb.zip", "config": "cinnamon-config.js"},
        "Winter (冬装)": {"path": "model/cinnamon-winter.pure.psb.zip", "config": "cinnamon-config.js"},
        "Yukata (浴衣)": {"path": "model/cinnamon-yukata.pure.psb.zip", "config": "cinnamon-config.js"},
    },
    "Coconut (椰子)": {
        "Casual (便服)": {"path": "model/coconut-casual.pure.psb.zip", "config": "coconut-config.js"},
        "Dress (礼服)": {"path": "model/coconut-dress.pure.psb.zip", "config": "coconut-config.js"},
        "Koneko (幼年)": {"path": "model/coconut-koneko.pure.psb.zip", "config": "kococonut-config.js"},
        "Maid (女仆装)": {"path": "model/coconut-maid.pure.psb.zip", "config": "coconut-config.js"},
        "Pajama (睡衣)": {"path": "model/coconut-pajama.pure.psb.zip", "config": "coconut-config.js"},
        "Santa (圣诞装)": {"path": "model/coconut-santa.pure.psb.zip", "config": "coconut-config.js"},
        "Teenage (少女)": {"path": "model/coconut-teenage.pure.psb.zip", "config": "coconut-config.js"},
        "WinterMaid (冬女仆)": {"path": "model/coconut-wintermaid.pure.psb.zip", "config": "coconut-config.js"},
        "Winter (冬装)": {"path": "model/coconut-winter.pure.psb.zip", "config": "coconut-config.js"},
        "Yukata (浴衣)": {"path": "model/coconut-yukata.pure.psb.zip", "config": "coconut-config.js"},
    },
    "Maple (枫)": {
        "Casual (便服)": {"path": "model/maple-casual.pure.psb.zip", "config": "maple-config.js"},
        "Dress (礼服)": {"path": "model/maple-dress.pure.psb.zip", "config": "maple-config.js"},
        "Maid (女仆装)": {"path": "model/maple-maid.pure.psb.zip", "config": "maple-config.js"},
        "Santa (圣诞装)": {"path": "model/maple-santa.pure.psb.zip", "config": "maple-config.js"},
        "Teenage (少女)": {"path": "model/maple-teenage.pure.psb.zip", "config": "maple-config.js"},
        "WinterMaid (冬女仆)": {"path": "model/maple-wintermaid.pure.psb.zip", "config": "maple-config.js"},
        "Winter (冬装)": {"path": "model/maple-winter.pure.psb.zip", "config": "maple-config.js"},
        "Yukata (浴衣)": {"path": "model/maple-yukata.pure.psb.zip", "config": "maple-config.js"},
    },
    "Vanilla (香草)": {
        "Casual (便服)": {"path": "model/vanilla-casual.pure.psb.zip", "config": "vanilla-config.js"},
        "Dress (礼服)": {"path": "model/vanilla-dress.pure.psb.zip", "config": "vanilla-config.js"},
        "Koneko (幼年)": {"path": "model/vanilla-koneko.pure.psb.zip", "config": "kovanilla-config.js"},
        "Lolita (洛丽塔)": {"path": "model/vanilla-lolita.pure.psb.zip", "config": "vanilla-config.js"},
        "Maid (女仆装)": {"path": "model/vanilla-maid.pure.psb.zip", "config": "vanilla-config.js"},
        "Pajama (睡衣)": {"path": "model/vanilla-pajama.pure.psb.zip", "config": "vanilla-config.js"},
        "Santa (圣诞装)": {"path": "model/vanilla-santa.pure.psb.zip", "config": "vanilla-config.js"},
        "Teenage (少女)": {"path": "model/vanilla-teenage.pure.psb.zip", "config": "vanilla-config.js"},
        "WinterMaid (冬女仆)": {"path": "model/vanilla-wintermaid.pure.psb.zip", "config": "vanilla-config.js"},
        "Winter (冬装)": {"path": "model/vanilla-winter.pure.psb.zip", "config": "vanilla-config.js"},
        "Yukata (浴衣)": {"path": "model/vanilla-yukata.pure.psb.zip", "config": "vanilla-config.js"},
    },
    "Milk (牛奶)": {
        "Teenage (少女)": {"path": "model/milk-teenage.pure.psb.zip", "config": "milk-config.js"},
        "Winter (冬装)": {"path": "model/milk-winter.pure.psb.zip", "config": "milk-config.js"},
    },
    "Fraise (草莓)": {
        "Maid (女仆装)": {"path": "model/fraise-maid.pure.psb.zip", "config": "fraise-config.js"},
    }
}

DEFAULT_CONFIG = {
    "model_path": "models/vanilla-maid.pure.psb.zip.zip",
    "config_js": "vanilla-config.js",
    "scale": 0.5,
    "window_width": 600,
    "window_height": 1000,
    "window_x": 100,
    "window_y": 100,
    "locked": False,
    "click_through": False
}

HTML_TEMPLATE = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {{ margin: 0; overflow: hidden; background-color: transparent; font-family: sans-serif; }}
        /* 使用 image-rendering: high-quality 提示浏览器使用高质量缩放算法 
           注意：Canvas 实际像素是屏幕的2倍，这里 CSS 强制撑满窗口，从而产生缩小（平滑）效果
        */
        canvas {{ 
            display: block; 
            width: 100%; 
            height: 100%; 
            opacity: 0; 
            transition: opacity 0.5s ease;
            image-rendering: -webkit-optimize-contrast; 
        }}
        canvas.loaded {{ opacity: 1; }}
        #loader-container {{
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            display: flex; justify-content: center; align-items: center;
            background: transparent; z-index: 999;
            transition: opacity 0.5s ease;
            pointer-events: none;
        }}
        .spinner {{ animation: rotate 2s linear infinite; z-index: 2; width: 50px; height: 50px; }}
        .path {{
            stroke: #ff69b4; stroke-linecap: round;
            animation: dash 1.5s ease-in-out infinite;
        }}
        @keyframes rotate {{ 100% {{ transform: rotate(360deg); }} }}
        @keyframes dash {{
            0% {{ stroke-dasharray: 1, 150; stroke-dashoffset: 0; }}
            50% {{ stroke-dasharray: 90, 150; stroke-dashoffset: -35; }}
            100% {{ stroke-dasharray: 90, 150; stroke-dashoffset: -124; }}
        }}
        .fade-out {{ opacity: 0; }}
    </style>
    <script>
        var Module = {{
            TOTAL_MEMORY: 536870912,
            errorhandler: null,
            onAbort: function(what) {{ console.error("Emscripten Aborted:", what); }}
        }};
    </script>
    <script src="{LOCAL_SERVER}/fflate.js"></script>
    <script src="{LOCAL_SERVER}/FreeMoteDriver.js"></script>
    <script src="{LOCAL_SERVER}/emoteplayer.js"></script>
    <script src="__CONFIG_URL__"></script>
</head>
<body>
    <div id="loader-container">
        <svg class="spinner" viewBox="0 0 50 50">
            <circle class="path" cx="25" cy="25" r="20" fill="none" stroke-width="5"></circle>
        </svg>
    </div>
    <canvas id="canvas"></canvas>
    <script>
        var player = null;
        var modelUrl = '__MODEL_URL__';
        var reactionConfig = {{}};
        var currentScale = __INIT_SCALE__;
        var isTouching = false;
        
        // === 优化点 1: 定义超采样倍率 (2.0 = 2倍抗锯齿) ===
        var ratioMultiplier = 2.0; 

        if (typeof getConfig === 'function') {{
            reactionConfig = getConfig();
        }}

        async function init() {{
            var canvas = document.getElementById('canvas');

            resizeCanvas();
            window.onresize = resizeCanvas;

            // === 优化点 2: 传递给 EmotePlayer 的也是高 DPI 分辨率 ===
            if (EmotePlayer.createRenderCanvas) {{
                var dpr = (window.devicePixelRatio || 1) * ratioMultiplier;
                EmotePlayer.createRenderCanvas(window.innerWidth * dpr, window.innerHeight * dpr);
            }}
            player = new EmotePlayer(canvas);

            try {{
                var finalUrl = modelUrl;
                if (modelUrl.endsWith('.zip')) {{
                    const resp = await fetch(modelUrl);
                    if (!resp.ok) throw new Error("Fetch failed");
                    const zipData = new Uint8Array(await resp.arrayBuffer());
                    const files = await new Promise((resolve, reject) => {{
                        fflate.unzip(zipData, (err, unzipped) => {{
                            if (err) reject(err); else resolve(unzipped);
                        }});
                    }});
                    const binFileName = Object.keys(files).find(name => name.endsWith('.psb'));
                    if (!binFileName) throw new Error("No .psb in zip");
                    const blob = new Blob([files[binFileName]], {{ type: 'application/octet-stream' }});
                    finalUrl = URL.createObjectURL(blob);
                }}

                await player.promiseLoadDataFromURL(finalUrl);

                // === 优化点 3: 应用初始缩放时，乘以超采样倍率 ===
                player.scale = currentScale * ratioMultiplier;

                var c = player.coord;
                c[1] -= 40;
                player.coord = c;

                player.diffTimelineSlot4 = '差分用_waiting_loop';

                document.getElementById('loader-container').classList.add('fade-out');
                canvas.classList.add('loaded');

            }} catch (e) {{
                console.error("Load Error:", e);
                document.querySelector('.path').style.stroke = 'red';
            }}
        }}

        function resizeCanvas() {{
            var canvas = document.getElementById('canvas');
            // === 优化点 4: 画布物理分辨率为 屏幕像素 * 2，实现超采样 ===
            var dpr = (window.devicePixelRatio || 1) * ratioMultiplier;
            canvas.width = window.innerWidth * dpr;
            canvas.height = window.innerHeight * dpr;
            if (player) {{
                // 窗口大小改变时，保持视觉缩放比例正确
                player.scale = currentScale * ratioMultiplier;
            }}
        }}

        window.updateModelScale = function(s) {{
            currentScale = s;
            if(player) {{
                // 动态更新缩放时，同样乘以倍率
                player.scale = currentScale * ratioMultiplier;
            }}
        }};

        window.updateEyeTracking = function(x, y) {{
            if (!player) return;
            // 眼神追踪使用相对坐标(-1 到 1)，不需要修改倍率
            var rawX = x * 500; var rawY = y * 500;
            var len = Math.sqrt(rawX*rawX + rawY*rawY);
            var angle = Math.atan2(rawY, rawX);
            var c = Math.cos(angle); var s = Math.sin(angle);
            try {{
                player.setVariableDiff('eyetrack', 'face_eye_LR', len / 3 * c, 500, -1);
                player.setVariableDiff('eyetrack', 'face_eye_UD', len / 3 * s, 500, -1);
                if (len > 60) {{
                    player.setVariableDiff('eyetrack', 'head_slant', len / 12 * c, 1000, -1);
                    player.setVariableDiff('eyetrack', 'head_LR', len / 6 * c, 1000, -1);
                    player.setVariableDiff('eyetrack', 'head_UD', len / 6 * s, 1000, -1);
                }}
                if (len > 120) {{
                    player.setVariableDiff('eyetrack', 'body_slant', len / 18 * c, 2000, -1);
                    player.setVariableDiff('eyetrack', 'body_LR', len / 9 * c, 2000, -1);
                    player.setVariableDiff('eyetrack', 'body_UD', len / 9 * s, 2000, -1);
                }}
            }} catch(e) {{}}
        }};

        function applyReactionConfig(config) {{
            if(!config) return;
            player.mainTimelineLabel = config.mainTimelineLabel || '';
            player.diffTimelineSlot1 = config.diffTimelineSlot1 || '';
            player.diffTimelineSlot2 = config.diffTimelineSlot2 || '';
            if (config.audio) {{
                try {{
                    var audioPath = config.audio;
                    if(audioPath.startsWith('./')) audioPath = audioPath.substring(2);
                    var audio = new Audio(audioPath);
                    audio.volume = 1.0;
                    audio.play().catch(e => {{}});
                }} catch(e) {{ }}
            }}
            if (config.variables) {{
                config.variables.forEach(v => {{
                    player.setVariable(v.name, v.value, v.duration, v.delay || 0);
                }});
            }}
        }}

        window.handleClick = function(x, y) {{
            if (!player || isTouching) return;
            // === 优化点 5: 点击坐标修正 ===
            // 传入的 x, y 是窗口逻辑坐标。
            // 画布内部是高分辨率，所以需要乘以 dpr 和 ratioMultiplier
            var dpr = (window.devicePixelRatio || 1) * ratioMultiplier;
            var ev = {{ clientX: x * dpr, clientY: y * dpr }};
            
            const getPos = (name) => {{ try {{ return player.getMarkerPosition(name); }} catch(e) {{ return null; }} }};
            const calcDist = (nameA, nameB, extraY=0) => {{
                let cx, cy;
                const mA = getPos(nameA);
                const mB = nameB ? getPos(nameB) : null;
                if (mA && mB) {{ cx = (mA.clientX + mB.clientX) / 2; cy = (mA.clientY + mB.clientY) / 2; }}
                else if (mA) {{ cx = mA.clientX; cy = mA.clientY; }}
                else {{ return 9999; }}
                // 注意：EmotePlayer 的 getMarkerPosition 返回的通常是画布内坐标
                return Math.sqrt(Math.pow(cx - ev.clientX, 2) + Math.pow(cy + extraY - ev.clientY, 2));
            }};
            const bustLength = calcDist('bust');
            const eyeLength = calcDist('eye');
            const headLength = calcDist('headAX', 'headBX');
            const faceLength = calcDist('headAX', 'headBX', 40);
            const pantLength = calcDist('pantAX', 'pantBX');

            const tryReact = (dist, threshold, reactions) => {{
                // 阈值也需要适配高分屏吗？通常距离是像素单位，如果画面大了2倍，距离阈值也可以适当放宽
                // 但因为我们计算的是欧氏距离，保持原样通常也能触发，或者稍微乘以 ratioMultiplier
                if (dist < threshold * ratioMultiplier && reactions && reactions.length) {{
                    isTouching = true;
                    const selected = reactions[Math.floor(Math.random() * reactions.length)];
                    applyReactionConfig(selected.reaction);
                    setTimeout(() => {{
                        applyReactionConfig(selected.recovery);
                        isTouching = false;
                    }}, selected.duration);
                    return true;
                }}
                return false;
            }};
            // 稍微调大阈值以适应高分屏下的点击误差
            if (tryReact(bustLength, 100, reactionConfig.bust)) return;
            if (tryReact(eyeLength, 50, reactionConfig.eye)) return;
            if (tryReact(faceLength, 80, reactionConfig.face)) return;
            if (tryReact(headLength, 120, reactionConfig.head)) return;
            if (tryReact(pantLength, 180, reactionConfig.pant)) return;
        }};

        window.onload = init;
    </script>
</body>
</html>
"""

class ConfigManager:
    @staticmethod
    def load():
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    config = DEFAULT_CONFIG.copy()
                    config.update(data)
                    return config
            except Exception: pass
        return DEFAULT_CONFIG.copy()

    @staticmethod
    def save(data):
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception: pass

class SettingsDialog(QDialog):
    def __init__(self, current_scale, current_w, current_h, parent=None):
        super().__init__(parent)
        self.setWindowTitle("设置")
        layout = QFormLayout(self)

        self.scale_spin = QDoubleSpinBox()
        self.scale_spin.setRange(0.05, 3.0)
        self.scale_spin.setSingleStep(0.05)
        self.scale_spin.setValue(current_scale)
        layout.addRow("模型缩放 (Scale):", self.scale_spin)

        self.w_spin = QSpinBox()
        self.w_spin.setRange(200, 3000)
        self.w_spin.setValue(current_w)
        layout.addRow("窗口宽度:", self.w_spin)

        self.h_spin = QSpinBox()
        self.h_spin.setRange(200, 3000)
        self.h_spin.setValue(current_h)
        layout.addRow("窗口高度:", self.h_spin)

        btn = QPushButton("确定")
        btn.clicked.connect(self.accept)
        layout.addRow(btn)

    def get_values(self):
        return self.scale_spin.value(), self.w_spin.value(), self.h_spin.value()

class TransparentCover(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.parent_window = parent
        self.drag_start_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_pos = event.globalPosition().toPoint()
            if not self.parent_window.is_locked:
                self.drag_window_offset = self.drag_start_pos - self.parent_window.frameGeometry().topLeft()
        elif event.button() == Qt.MouseButton.RightButton:
            self.show_context_menu(event.globalPosition().toPoint())

    def mouseMoveEvent(self, event):
        if not self.parent_window.is_locked and event.buttons() & Qt.MouseButton.LeftButton and self.drag_start_pos:
            current_pos = event.globalPosition().toPoint()
            if (current_pos - self.drag_start_pos).manhattanLength() > 5:
                self.parent_window.move(current_pos - self.drag_window_offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.drag_start_pos:
            start = self.drag_start_pos
            end = event.globalPosition().toPoint()
            if (start - end).manhattanLength() < 5:
                local_pos = event.position().toPoint()
                self.parent_window.trigger_click(local_pos.x(), local_pos.y())
        self.drag_start_pos = None

    def show_context_menu(self, global_pos):
        menu = QMenu(self)

        switch_menu = menu.addMenu("切换角色")
        for char_name, outfits in MODEL_LIBRARY.items():
            char_menu = switch_menu.addMenu(char_name)
            for outfit_name, data in outfits.items():
                action = QAction(outfit_name, self)
                action.triggered.connect(lambda checked, d=data: self.parent_window.load_model(d["path"], d["config"]))
                char_menu.addAction(action)

        menu.addSeparator()

        lock_action = QAction("锁定位置", self)
        lock_action.setCheckable(True)
        lock_action.setChecked(self.parent_window.is_locked)
        if self.parent_window.is_click_through:
            lock_action.setEnabled(False)
        lock_action.triggered.connect(self.parent_window.toggle_lock)
        menu.addAction(lock_action)

        click_through_action = QAction("鼠标穿透 (Click Through)", self)
        click_through_action.setCheckable(True)
        click_through_action.setChecked(self.parent_window.is_click_through)
        click_through_action.triggered.connect(self.parent_window.toggle_click_through)
        menu.addAction(click_through_action)

        menu.addSeparator()
        act1 = QAction("设置", self); act1.triggered.connect(self.parent_window.open_settings_dialog); menu.addAction(act1)
        act2 = QAction("刷新页面", self); act2.triggered.connect(self.parent_window.webview.reload); menu.addAction(act2)

        # === 修复点 1: 右键菜单使用 quit_app ===
        act3 = QAction("退出程序", self); act3.triggered.connect(self.parent_window.quit_app); menu.addAction(act3)

        menu.exec(global_pos)

class FreeMotePet(QMainWindow):
    def __init__(self):
        super().__init__()
        self.base_flags = Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool
        self.setWindowFlags(self.base_flags)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.config = ConfigManager.load()
        self.current_scale = self.config.get("scale", 0.5)
        self.current_w = self.config.get("window_width", 600)
        self.current_h = self.config.get("window_height", 1000)

        self.is_locked = self.config.get("locked", False)
        self.is_click_through = self.config.get("click_through", False)
        self.current_model_path = self.config.get("model_path", "models/vanilla-maid.pure.psb.zip.zip")
        self.current_config_js = self.config.get("config_js", "vanilla-config.js")

        self.webview = QWebEngineView(self)
        self.webview.page().setBackgroundColor(Qt.GlobalColor.transparent)
        self.webview.settings().setAttribute(QWebEngineSettings.WebAttribute.PlaybackRequiresUserGesture, False)
        self.webview.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)

        self.cover = TransparentCover(self)

        self.load_model(self.current_model_path, self.current_config_js)
        self.resize(self.current_w, self.current_h)
        self.move(self.config.get("window_x", 100), self.config.get("window_y", 100))

        if self.is_click_through:
            self.set_window_click_through(True)

        self.init_tray_icon()

        self.tracker_timer = QTimer(self)
        self.tracker_timer.timeout.connect(self.update_eye_tracking)
        self.tracker_timer.start(50)

    def init_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(self)
        icon_path = "icon.png"
        if os.path.exists(icon_path):
            self.tray_icon.setIcon(QIcon(icon_path))
        else:
            self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))
        self.tray_icon.setToolTip("FreeMote Desktop Pet")
        tray_menu = QMenu()
        self.show_hide_action = QAction("隐藏", self)
        self.show_hide_action.triggered.connect(self.toggle_visibility)
        tray_menu.addAction(self.show_hide_action)
        tray_menu.addSeparator()
        self.lock_action = QAction("锁定位置", self)
        self.lock_action.setCheckable(True)
        self.lock_action.setChecked(self.is_locked)
        if self.is_click_through:
            self.lock_action.setEnabled(False)
            self.lock_action.setChecked(True)
        self.lock_action.triggered.connect(self.toggle_lock)
        tray_menu.addAction(self.lock_action)
        self.click_through_action_tray = QAction("鼠标穿透", self)
        self.click_through_action_tray.setCheckable(True)
        self.click_through_action_tray.setChecked(self.is_click_through)
        self.click_through_action_tray.triggered.connect(self.toggle_click_through)
        tray_menu.addAction(self.click_through_action_tray)
        tray_menu.addSeparator()

        # === 修复点 2: 托盘菜单使用 quit_app ===
        quit_action = QAction("退出", self)
        quit_action.triggered.connect(self.quit_app)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.on_tray_icon_activated)

    # === 修复点 3: 专门的完全退出函数 ===
    def quit_app(self):
        # 1. 停止计时器
        if self.tracker_timer.isActive():
            self.tracker_timer.stop()
        # 2. 显式隐藏托盘图标（关键步骤，否则图标会导致进程残留）
        self.tray_icon.hide()
        # 3. 触发关闭事件以保存配置
        self.close()
        # 4. 强制退出应用程序
        QCoreApplication.quit()

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.toggle_visibility()

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
            self.show_hide_action.setText("显示")
        else:
            self.show()
            self.show_hide_action.setText("隐藏")
            self.raise_()

    def toggle_lock(self):
        if self.is_click_through: return
        self.is_locked = not self.is_locked
        self.lock_action.setChecked(self.is_locked)
        self.config["locked"] = self.is_locked
        ConfigManager.save(self.config)

    def toggle_click_through(self):
        self.is_click_through = not self.is_click_through
        self.set_window_click_through(self.is_click_through)
        self.config["click_through"] = self.is_click_through
        self.config["locked"] = self.is_locked
        ConfigManager.save(self.config)
        self.click_through_action_tray.setChecked(self.is_click_through)
        self.lock_action.setChecked(self.is_locked)
        self.lock_action.setEnabled(not self.is_click_through)

    def set_window_click_through(self, enabled):
        flags = self.base_flags
        if enabled:
            flags |= Qt.WindowType.WindowTransparentForInput
            self.is_locked = True
        self.setWindowFlags(flags)
        self.show()
        self.raise_()

    def load_model(self, model_path, config_js_file):
        print(f"Switching to: {model_path} with config: {config_js_file}")
        self.current_model_path = model_path
        self.current_config_js = config_js_file
        full_model_url = f"{LOCAL_SERVER}/{model_path}"
        full_config_url = f"{LOCAL_SERVER}/config/{config_js_file}"

        final_html = HTML_TEMPLATE.replace('__MODEL_URL__', full_model_url) \
                                  .replace('__CONFIG_URL__', full_config_url) \
                                  .replace('__INIT_SCALE__', str(self.current_scale))

        self.webview.setHtml(final_html, QUrl(LOCAL_SERVER + "/"))
        self.config["model_path"] = model_path
        self.config["config_js"] = config_js_file

    def trigger_click(self, x, y):
        self.webview.page().runJavaScript(f"if(window.handleClick) handleClick({x}, {y});")

    def open_settings_dialog(self):
        dialog = SettingsDialog(self.current_scale, self.current_w, self.current_h, self)
        if dialog.exec():
            s, w, h = dialog.get_values()

            self.current_scale = s
            self.current_w = w
            self.current_h = h

            self.resize(w, h)
            self.webview.page().runJavaScript(f"if(window.updateModelScale) updateModelScale({s});")

            self.config["scale"] = s
            self.config["window_width"] = w
            self.config["window_height"] = h
            ConfigManager.save(self.config)

    def update_eye_tracking(self):
        if not self.isVisible(): return
        global_cursor = QCursor.pos()
        window_geo = self.geometry()
        cx, cy = window_geo.x() + window_geo.width()/2, window_geo.y() + window_geo.height()/2
        dx, dy = global_cursor.x() - cx, global_cursor.y() - cy
        nx = max(-1.0, min(1.0, dx / 1000.0))
        ny = max(-1.0, min(1.0, dy / 800.0))
        self.webview.page().runJavaScript(f"if(window.updateEyeTracking) updateEyeTracking({nx:.3f}, {ny:.3f});")

    def resizeEvent(self, event):
        self.webview.resize(self.width(), self.height())
        self.cover.resize(self.width(), self.height())
        super().resizeEvent(event)

    def closeEvent(self, event):
        self.config["window_x"] = self.x(); self.config["window_y"] = self.y()
        self.config["locked"] = self.is_locked
        self.config["click_through"] = self.is_click_through
        self.config["window_width"] = self.width()
        self.config["window_height"] = self.height()
        ConfigManager.save(self.config)
        event.accept()

if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_API"] = "pyqt6"
    sys.argv.append("--disable-web-security")
    sys.argv.append("--autoplay-policy=no-user-gesture-required")
    sys.argv.append("--enable-gpu-rasterization")
    sys.argv.append("--ignore-gpu-blocklist")
    sys.argv.append("--enable-webgl-image-chromium")
    sys.argv.append("--gl-options=msaa-sample-count=4")

    app = QApplication(sys.argv)

    # === 建议添加: 确保在最后一个窗口关闭时不自动退出，由我们的 quit_app 接管 ===
    app.setQuitOnLastWindowClosed(False)

    pet = FreeMotePet()
    pet.show()
    sys.exit(app.exec())
