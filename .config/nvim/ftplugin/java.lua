
require('jdtls').start_or_attach({cmd = {'java-lsp.sh'}})
capabilities=capabilities


--Keys

local opts = {noremap=true, silent=true}

vim.api.nvim_set_keymap('n', 'gD', '<cmd>lua vim.lsp.buf.declaration()<CR>', opts)
vim.api.nvim_set_keymap('n', 'gd', '<cmd>lua vim.lsp.buf.definition()<CR>', opts)
vim.api.nvim_set_keymap('n', 'K', '<cmd>lua vim.lsp.buf.hover()<CR>', opts)
vim.api.nvim_set_keymap('n', 'gi', '<cmd>lua vim.lsp.buf.implementation()<CR>', opts)
--vim.api.nvim_set_keymap('n', '<C-k>', '<cmd>lua vim.lsp.buf.signature_help()<CR>', opts)
--vim.api.nvim_set_keymap('n', '<space>wa', '<cmd>lua vim.lsp.buf.add_workspace_folder()<CR>', opts)
--vim.api.nvim_set_keymap('n', '<space>wr', '<cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>', opts)
--vim.api.nvim_set_keymap('n', '<space>i', '<cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>', opts)
vim.api.nvim_set_keymap('n', 'gt', '<cmd>lua vim.lsp.buf.type_definition()<CR>', opts)
vim.api.nvim_set_keymap('n', 'gr', '<cmd>lua vim.lsp.buf.rename()<CR>', opts)
vim.api.nvim_set_keymap('n', 'gx', '<cmd>lua vim.lsp.buf.code_action()<CR>', opts)
vim.api.nvim_set_keymap('n', '<leader>r', '<cmd>lua vim.lsp.buf.references()<CR>', opts)
vim.api.nvim_set_keymap('n', '<space>f', '<cmd>lua vim.lsp.buf.formatting()<CR>', opts)

--vim.api.nvim_set_keymap('n', '<leader>x', '<cmd>lua require(\'jdtls\').code_action()<CR>', {silent = true})

---for Lspsaga
--vim.cmd([[
--nnoremap <silent> gr :Lspsaga rename<cr>
--nnoremap <silent> gx :Lspsaga code_action<cr>
--nnoremap <silent> gx :<c-u>Lspsaga range_code_action<cr>
--nnoremap <silent> K  :Lspsaga hover_doc<cr>
--nnoremap <silent> go :Lspsaga show_line_diagnostics<cr>
--nnoremap <silent> gj :Lspsaga diagnostic_jump_next<cr>
--nnoremap <silent> gk :Lspsaga diagnostic_jump_prev<cr>
--nnoremap <silent> <C-u> :lua require('lspsaga.action').smart_scroll_with_saga(-1)<cr>
--nnoremap <silent> <C-d> :lua require('lspsaga.action').smart_scroll_with_saga(1)<cr>

--]])
