-----------------------------------------------------------
-- Neovim settings
--- General Neovim settings
-----------------------------------------------------------

-----------------------------------------------------------
-- Neovim API aliases
-----------------------------------------------------------
--local map = vim.api.nvim_set_keymap  -- set global keymap
local cmd = vim.cmd             -- execute Vim commands
local exec = vim.api.nvim_exec  -- execute Vimscript
local fn = vim.fn               -- call Vim functions
local g = vim.g                 -- global variables
local set = vim.opt             -- global/buffer/windows-scoped options

-----------------------------------------------------------
-- General
-----------------------------------------------------------
g.mapleader = ','             -- change leader to a comma
set.mouse = 'a'               -- enable mouse support
set.swapfile = false          -- don't use swapfile
set.encoding = 'utf-8'        -- the encoding displayed
set.fileencoding = 'utf-8'    -- the encoding written to file
set.clipboard = 'unnamedplus' -- copy/paste to system clipboard
set.splitbelow = true
set.splitright = true


-----------------------------------------------------------
-- Neovim UI
-----------------------------------------------------------
set.syntax = 'enable'         -- enable syntax highlighting
set.wrap = false              -- display long line as just one
set.showmode = false          -- dont show things like Insert
set.signcolumn = 'auto'     -- set sign column
set.number = true             -- show line number
set.relativenumber = true     -- show relativenumber on number line
set.showmatch = true          -- highlight matching parenthesis
set.foldmethod = 'marker'     -- enable folding (default 'foldmarker')
--set.colorcolumn = '80'        -- line lenght marker at 80 columns
set.splitright = true         -- vertical split to the right
set.splitbelow = true         -- orizontal split to the bottom
set.ignorecase = true         -- ignore case letters when search
set.smartcase = true          -- ignore lowercase for the whole pattern
set.cursorline = true         -- Enable highlighting of current line
set.conceallevel = 0          -- so that I can see `` in markdown files
-------------------------------------------------------------------------
-- Editor UI
-------------------------------------------------------------------------
set.pumblend = 10            -- Enable transparency for popup menu
set.pumheight = 10           -- height of popup menu
set.pumwidth = 50            -- width of popup menu
set.cmdheight = 2            -- more space for displaying msg
set.updatetime = 250         -- faster completion
set.timeoutlen = 500         -- by default timeoutlen is 1000ms

-- remove whitespace on save
cmd[[au BufWritePre * :%s/\s\+$//e]]

-- highlight on yank
exec([[
  augroup YankHighlight
    autocmd!
    autocmd TextYankPost * silent! lua vim.highlight.on_yank{higroup="IncSearch", timeout=700}
  augroup end
]], false)

-----------------------------------------------------------
-- Memory, CPU
-----------------------------------------------------------
set.hidden = true         -- enable background buffers
set.history = 100         -- remember n lines in history
set.lazyredraw = true     -- faster scrolling
set.synmaxcol = 240       -- max column for syntax highlight

-----------------------------------------------------------
-- Colorscheme
-----------------------------------------------------------
set.termguicolors = true          -- enable 24-bit RGB colors

--set.t_Co = 256
--cmd[[colorscheme catppuccin]]        -- set colorscheme

-----------------------------------------------------------
-- Tabs, indent
-----------------------------------------------------------
set.smarttab = true       -- makes tabbing smarter
set.expandtab = true      -- use spaces instead of tabs
set.shiftwidth = 4        -- shift 4 spaces when tab
set.softtabstop = 4
set.tabstop = 4           -- 1 tab == 4 spaces
--set.smartindent = true    -- autoindent new lines

-- don't auto commenting new lines
cmd[[au BufEnter * set fo-=c fo-=r fo-=o]]

-- remove line lenght marker for selected filetypes
cmd[[
  autocmd FileType text,markdown,xml,html,xhtml,javascript setlocal cc=0
]]

-- 2 spaces for selected filetypes
cmd[[
  autocmd FileType xml,html,xhtml,css,scss,javascript,lua,yaml setlocal shiftwidth=2 tabstop=2
]]

-- 8 spaces for Go files
cmd[[autocmd FileType go setlocal shiftwidth=8 tabstop=8]]

-- IndentLine
--g.indentLine_setColors = '#e55a1c'  -- set indentLine color
g.indentLine_char = '|'       -- set indentLine character

-- disable IndentLine for markdown files (avoid concealing)
cmd[[
	autocmd FileType markdown let g:indentLine_enabled=0
]]

-----------------------------------------------------------
-- Autocompletion
-----------------------------------------------------------
set.completeopt = 'menuone,noselect,noinsert' -- completion options
--set.shortmess = 'c' 	-- don't show completion messages

-------------------------------------------------------------------------
-- DIAGNOSTIC settings
-----------------------------------------------------------------------




