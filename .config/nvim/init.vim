

highlight clear cursorline

set iskeyword+=-                        " treat dash separated words as a word text object"
set formatoptions-=cro                  " Stop newline continution of comments
"set autochdir                           " Your working directory will always be the same as your working directory

au! BufWritePost $MYVIMRC source %      " auto source when writing to init.vm alternatively you can run :source $MYVIMRC

" You can't stop me
cmap w!! w !sudo tee %

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Vim-Floaterm
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap   <silent>   <F7>    :FloatermNew zsh<CR>
tnoremap   <silent>   <F7>    <C-\><C-n>:FloatermNew zsh<CR>
nnoremap   <silent>   <F8>    :FloatermPrev<CR>
tnoremap   <silent>   <F8>    <C-\><C-n>:FloatermPrev<CR>
nnoremap   <silent>   <F9>    :FloatermNext<CR>
tnoremap   <silent>   <F9>    <C-\><C-n>:FloatermNext<CR>
nnoremap   <silent>   <F12>   :FloatermToggle zsh<CR>
tnoremap   <silent>   <F12>   <C-\><C-n>:FloatermToggle zsh<CR>
nnoremap   <silent>   <F10>   :FloatermKill<CR>

nnoremap   <silent>   <leader>r :FloatermNew ranger<CR>    "for ranger

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" TERMINAL_SETTINGS
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
autocmd BufEnter * silent! lcd %:p:h  " Open terminal to woking directory
map <F6> :let $VIM_DIR=expand('%:p:h')<CR>:Vterm<CR>cd $VIM_DIR<CR> " toggle Vertical terminal by key press
"map <F7> :let $VIM_DIR=expand('%:p:h')<CR>:Hterm<CR>cd $VIM_DIR<CR> " toggle Horizontal terminal by key press


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" SOURCE_FILE
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"source ~/.config/nvim/plug/coc.vim
source ~/.config/nvim/color/dark.vim

call plug#begin('~/.local/share/nvim/plugged')
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Statusline
Plug 'nvim-lualine/lualine.nvim'

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Editing tools
Plug 'norcalli/nvim-colorizer.lua'    "colorizer
Plug 'p00f/nvim-ts-rainbow'           "bracket colorizer
Plug 'lukas-reineke/indent-blankline.nvim' " indentLine
Plug 'windwp/nvim-autopairs'           "autopairs
Plug 'xiyaowong/nvim-transparent'      " nvim-transparent
"Plug 'voldikss/vim-floaterm'           " vim-floaterm
" Using Vim-Plug:
Plug 'Mofiqul/dracula.nvim'            " DRACULA
"Plug 'tanvirtin/monokai.nvim'          " MONOKAI
"Plug 'kyazdani42/nvim-palenight.lua'    " palenight
"Plug 'folke/tokyonight.nvim', { 'branch': 'main' }  " tokyonight
"Plug 'navarasu/onedark.nvim'                " OneDark

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Treesitter
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'nvim-treesitter/playground'

" Telescope
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'nvim-telescope/telescope-ui-select.nvim'
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Icons
Plug 'ryanoasis/vim-devicons' " Icons for Statusline
Plug 'kyazdani42/nvim-web-devicons' " for file icons
Plug 'yamatsum/nvim-nonicons'
" Nvim_Tree
Plug 'kyazdani42/nvim-tree.lua'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" nvim-lsp
Plug 'neovim/nvim-lspconfig'     " nvim-lsp
Plug 'mfussenegger/nvim-jdtls'   " required for java
"Plug 'tami5/lspsaga.nvim'

" Nvim_cmp
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-cmdline'

" Vsnip
Plug 'hrsh7th/cmp-vsnip'
Plug 'hrsh7th/vim-vsnip'
Plug 'rafamadriz/friendly-snippets'     "vs code like Snippet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" UltiSnip
"Plug 'SirVer/ultisnips'
"Plug 'quangnguyen30192/cmp-nvim-ultisnips'
"Plug 'honza/vim-snippets'

call plug#end()




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Splits and Tabbed Files
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


" Remap splits navigation to just CTRL + hjkl
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" Make adjusing split sizes a bit more friendly
noremap <silent> <C-Left> :vertical resize +3<CR>
noremap <silent> <C-Right> :vertical resize -3<CR>
noremap <silent> <C-Up> :resize +3<CR>
noremap <silent> <C-Down> :resize -3<CR>

" Change 2 split windows from vert to horiz or horiz to vert
map <Leader>th <C-w>t<C-w>H
map <Leader>tk <C-w>t<C-w>K

" Removes pipes | that act as seperators on splits
" set fillchars+=vert:\

" Terminal
command Vterm :vsplit | :terminal fish
command Hterm :split | :terminal fish


" require lua
:lua <<EOF
-----------------------------------------------------------
-- Import Lua modules
-----------------------------------------------------------
require('settings')                 -- settings
require('keymaps')                  -- keymaps
require('Lsp-UI')                   -- lsp-ui
--require('lspsaga')                  -- lspSaga
require('plugins/transparent')      -- transparent
require('plugins/nvim-tree')        -- file manager
require('plugins/colorizer')        -- colorizer
require('plugins/indent_blankline') -- indentLine
require('plugins/autopairs')        -- autopairs
require('plugins/lualine')          -- Statusline
require('plugins/nvim-treesitter')  -- treesitter
require('plugins/telescope')        -- Telescope
require('plugins/nonicons')         -- icons
require('plugins/nvim-lspconfig')   -- nvim-lspconfig
require('plugins/nvim-cmp')         -- nvim_cmp
--require('plugins/lspsaga')          -- lsp floating window

EOF

"COLORSCHEMES


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" highlight
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Diagnostic windows
highlight NormalFloat     guibg='#001f2335'       gui=bold
highlight FloatBorder     guifg='#ff0000'       guibg='#00161616'     gui=bold

" nvim-cmp menu
"highlight CmpItemAbbr                  guifg='#ffffff'    guibg=none      gui=bold
highlight CmpItemAbbrDeprecated        guifg='#808080'    guibg=none         gui=strikethrough
highlight CmpItemAbbrMatch             guifg='#db2d20'    guibg=none         gui=bold
highlight CmpItemAbbrMatchFuzzy        guifg=none         guibg=none         gui=bold

highlight CmpItemKindVariable          guifg='#00e0c4'    guibg=none         gui=bold
highlight CmpItemKindInterface         guifg='#00ffae'    guibg=none         gui=bold
highlight CmpKindText                  guifg='#00ffae'    guibg=none         gui=bold

highlight CmpItemKindFunction          guifg='#fd5ff1'    guibg=none         gui=bold
highlight CmpItemKindMethod            guifg='#fd5ff1'    guibg=none         gui=bold

highlight CmpItemKindKeyword           guifg='#0000ff'    guibg=none         gui=bold
highlight CmpItemKindProperty          guifg='#0000ff'    guibg=none         gui=bold
highlight CmpItemKindUnit              guifg='#0000ff'    guibg=none         gui=bold

highlight CmpItemKindClass             guifg='#fdf908'    guibg=none         gui=bold
highlight CmpItemKindModule            guifg='#fdf908'    guibg=none         gui=bold

highlight CmpItemKindSnippet           guifg='#01a252'    guibg=none         gui=bold

highlight CmpItemMenu                  guifg='#ff0883'    guibg=none         gui=bold

highlight Pmenu                        guifg='#ffffff'    guibg='#000000'    gui=bold
highlight PmenuSel                     guibg='#5b6268'    guifg=none

" Vim-Floaterm
hi FloatermNC                          guibg=gray
hi Floaterm                            guibg=none
hi FloatermBorder                      guibg=none         guifg='#ff0000'

"set background=dark
colorscheme dracula
